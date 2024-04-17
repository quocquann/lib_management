from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
from django.core.cache import cache
import pandas as pd
from library.models import DetailBorrow

def get_relate_book():
    print("get relate book")
    detail_borrows = DetailBorrow.objects.all().order_by("-pk")[:500]
    data = list(detail_borrows.values("copy_id", "borrow_id"))
    df = pd.DataFrame(data)
    
    borrow_list = []
    for i in df['borrow_id'].unique():
        tlist = list(set(df.loc[df['borrow_id'] == i]['copy_id']))
        if len(tlist) > 0:
            borrow_list.append(tlist)
            
    te = TransactionEncoder()
    te_ary = te.fit(borrow_list).transform(borrow_list)
    new_df = pd.DataFrame(te_ary, columns=te.columns_)

    MIN_SUP = 0.001
    MIN_CONF = 0.2
    frequent_itemsets = apriori(new_df, min_support=MIN_SUP, use_colnames=True)
    rules = association_rules(frequent_itemsets, min_threshold=MIN_CONF).sort_values('confidence', ascending=False)

    cache.set("association_rules", rules)