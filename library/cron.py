from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
from django.core.cache import cache
import pandas as pd
from library.models import DetailBorrow, BookCopy
from datetime import timedelta
import os


def get_relate_book():
    print("get relate book")
    detail_borrows = DetailBorrow.objects.all().order_by("-pk")
    data = list(detail_borrows.values("copy_id", "borrow_id"))
    df = pd.DataFrame(data)
    
    borrow_list = []
    for i in df['borrow_id'].unique():
        copy_ids = list(set(df.loc[df['borrow_id'] == i]['copy_id']))
        blist = BookCopy.objects.filter(pk__in=copy_ids).values_list("book", flat=True)
        if len(blist) > 0:
            borrow_list.append(blist)
            
    te = TransactionEncoder()
    te_ary = te.fit(borrow_list).transform(borrow_list)
    new_df = pd.DataFrame(te_ary, columns=te.columns_)

    MIN_SUP = os.environ.get("MIN_SUP")
    MIN_CONF = os.environ.get("MIN_CONF")
    frequent_itemsets = apriori(new_df, min_support=MIN_SUP, use_colnames=True)
    rules = association_rules(frequent_itemsets, min_threshold=MIN_CONF).sort_values('confidence', ascending=False)

    timeout = timedelta(days=60)
    cache.set("association_rules", rules, timeout=timeout.total_seconds())