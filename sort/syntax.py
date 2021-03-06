from os.path import basename
from TabsExtra import tab_sort_helper as tsh


def run(views, view_data):
    for v in views:
        view_data.append(
            (
                tsh.numeric_sort(v.settings().get('syntax', '')),
                tsh.numeric_sort(basename(v.file_name() if v.file_name() else '').lower()),
                v
            )
        )
