import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lib_management.settings")

django.setup()

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
from django.core.cache import cache
import pandas as pd
from library.models import DetailBorrow
import datetime


def get_relate_book():
    # end_date = datetime.date.today()
    # start_date = end_date - datetime.timedelta(30)
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

    frequent_itemsets = apriori(new_df, min_support=0.001, use_colnames=True)
    print(frequent_itemsets.sort_values("support", ascending=False))
    rules = association_rules(frequent_itemsets, min_threshold=0.01).sort_values('confidence', ascending=False)
    print(rules)
    cache.set("rules", rules)

if __name__ == '__main__':
    get_relate_book()