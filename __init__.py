import operator
from functools import partial, reduce
from copy import deepcopy
from pprint import pprint
from cprinter import TC
from flatten_any_dict_iterable_or_whatsoever import (
    set_in_original_iter,
    get_from_original_iter,
)
from useful_functions_easier_life import NamedFunction

from flatten_any_dict_iterable_or_whatsoever import fla_tu


def return_string(_):
    return str(_)


# def series_to_dataframe(
#     df: Union[pd.Series, pd.DataFrame]
# ) -> (Union[pd.Series, pd.DataFrame], bool):
#     dataf = df
#     isseries = False
#     if isinstance(dataf, pd.Series):
#         columnname = dataf.name
#         dataf = dataf.to_frame()
#
#         try:
#             dataf.columns = [columnname]
#         except Exception:
#             dataf.index = [columnname]
#             dataf = dataf.T
#         isseries = True
#
#     return dataf, isseries


class NestedNop:
    """
    dictoriginal=data={'level1': {'t1': {'s1': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9},
                   's2': {'col1': 1, 'col2': 5, 'col3': 4, 'col4': 8},
                   's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 9},
                   's4': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9}},
            't2': {'s1': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9},
                   's2': {'col1': 1, 'col2': 5, 'col3': 4, 'col4': 8},
                   's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 9},
                   's4': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9}},
            't3': {'s1': {'col1': 1, 'col2': 2, 'col3': 3, 'col4': 4},
                   's2': {'col1': 5, 'col2': 6, 'col3': 7, 'col4': 8},
                   's3': {'col1': 9, 'col2': 10, 'col3': 11, 'col4': 12},
                   's4': {'col1': 13, 'col2': 14, 'col3': 15, 'col4': 16}}},
    'level2': {'t1': {'s1': {'col1': 5, 'col2': 4, 'col3': 9, 'col4': 9},
                   's2': {'col1': 1, 'col2': 5, 'col3': 4, 'col4': 5},
                   's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 13},
                   's4': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 20}},
            't2': {'s1': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9},
                   's2': {'col1': 1, 'col2': 5, 'col3': 4, 'col4': 8},
                   's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 9},
                   's4': {'col1': 5, 'col2': 4, 'col3': 4, 'col4': 9}},
            't3': {'s1': {'col1': 1, 'col2': 2, 'col3': 3, 'col4': 4},
                   's2': {'col1': 5, 'col2': 6, 'col3': 7, 'col4': 8},
                   's3': {'col1': 9, 'col2': 10, 'col3': 11, 'col4': 12},
                   's4': {'col1': 13, 'col2': 14, 'col3': 15, 'col4': 16}}}}


    nest=NestedNop(dictoriginal)
    for key, item in nest.iterable_flat.items():
        if item['get_value']() == 4 and key[-1] == 'col3':
            item['set_value'](400000000000000)

    updatediter = nest.get_updated_iterable()


    updatediter
    {'level1': {'t1': {'s1': {'col1': 5,
        'col2': 4,
        'col3': 400000000000000,
        'col4': 9},
       's2': {'col1': 1, 'col2': 5, 'col3': 400000000000000, 'col4': 8},
       's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 9},
       's4': {'col1': 5, 'col2': 4, 'col3': 400000000000000, 'col4': 9}},
      't2': {'s1': {'col1': 5, 'col2': 4, 'col3': 400000000000000, 'col4': 9},
       's2': {'col1': 1, 'col2': 5, 'col3': 400000000000000, 'col4': 8},
       's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 9},
       's4': {'col1': 5, 'col2': 4, 'col3': 400000000000000, 'col4': 9}},
      't3': {'s1': {'col1': 1, 'col2': 2, 'col3': 3, 'col4': 4},
       's2': {'col1': 5, 'col2': 6, 'col3': 7, 'col4': 8},
       's3': {'col1': 9, 'col2': 10, 'col3': 11, 'col4': 12},
       's4': {'col1': 13, 'col2': 14, 'col3': 15, 'col4': 16}}},
     'level2': {'t1': {'s1': {'col1': 5, 'col2': 4, 'col3': 9, 'col4': 9},
       's2': {'col1': 1, 'col2': 5, 'col3': 400000000000000, 'col4': 5},
       's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 13},
       's4': {'col1': 5, 'col2': 4, 'col3': 400000000000000, 'col4': 20}},
      't2': {'s1': {'col1': 5, 'col2': 4, 'col3': 400000000000000, 'col4': 9},
       's2': {'col1': 1, 'col2': 5, 'col3': 400000000000000, 'col4': 8},
       's3': {'col1': 11, 'col2': 8, 'col3': 2, 'col4': 9},
       's4': {'col1': 5, 'col2': 4, 'col3': 400000000000000, 'col4': 9}},
      't3': {'s1': {'col1': 1, 'col2': 2, 'col3': 3, 'col4': 4},
       's2': {'col1': 5, 'col2': 6, 'col3': 7, 'col4': 8},
       's3': {'col1': 9, 'col2': 10, 'col3': 11, 'col4': 12},
       's4': {'col1': 13, 'col2': 14, 'col3': 15, 'col4': 16}}}}

    """

    def __init__(
        self,
        iterable,
        disable_str_repr: bool = False,
        tuplecheck: bool = True,
        pandas_loc_or_iloc: str = "iloc",
    ):
        try:
            if "DataFrame" in str(type(iterable)) or "Series" in str(type(iterable)):
                ispandas = True
            else:
                ispandas = False
        except Exception:
            ispandas = False
        self.iterable = deepcopy(iterable)
        self.iterable_original = deepcopy(iterable)
        self.disable_str_repr = disable_str_repr
        self.tuplecheck = tuplecheck
        self.iterable_list = []
        self.ispandas = ispandas
        self.loc_or_iloc = pandas_loc_or_iloc
        self.get_iterable_list()
        self.iterable_flat = {}
        if ispandas is False:
            self.get_flat_iter()

    def __str__(self):
        if self.disable_str_repr is True:
            return ""
        print("")
        print(
            TC(
                '\nNestedNop.iterable_flat -> This is a flat dict of your original iterable.\nWhen you change a value here by using NestedNop.iterable_flat["set_value"]()\nIt will also change in NestedNop.iterable_original\n'
            ).bg_black.fg_yellow
        )
        print("")

        pprint(self.iterable_flat, width=1, indent=4)
        print("")

        print(
            TC(
                "\nYour original iterable -> NestedNop.iterable_original\n"
            ).bg_black.fg_pink
        )
        print("")

        pprint(self.iterable_original, width=200)
        print("")

        print(TC("\nThe updated iterable -> NestedNop.iterable\n").bg_black.fg_pink)
        print("")

        pprint(self.iterable, width=200)
        print("")

        return ""

    def __repr__(self):
        return self.__str__()

    def get_iterable_list(self):
        if (self.ispandas is False) or (
            self.ispandas is True and self.loc_or_iloc == "loc"
        ):
            self.iterable_list = [
                (
                    xx[0],
                    xx[1][-1],
                    reduce(operator.getitem, xx[1][:-1], self.iterable),
                    xx[1],
                )
                for xx in (fla_tu(self.iterable))
                if any(self.iterable)
            ]
        else:
            indexlookup, collookup = NestedNop.get_iloc_from_loc(df=self.iterable)
            self.iterable_list = (
                (
                    (
                        xx[0],
                        xx[1][-1],
                        reduce(operator.getitem, xx[1], self.iterable),
                        (collookup.get(xx[1][0]), indexlookup.get(xx[1][1]))
                        + xx[1][2:],
                    ),
                    (
                        xx[0],
                        xx[1][-1],
                        reduce(operator.getitem, xx[1], self.iterable),
                        xx[1],
                    ),
                )
                for xx in fla_tu(self.iterable)
            )

    @staticmethod
    def get_iloc_from_loc(df):
        return (
            {v: k for k, v in enumerate(df.index.to_list())},
            {v: k for k, v in enumerate(df.columns.to_list())},
        )

    def get_updated_iterable(self):
        return self.iterable

    def get_flat_iter(self):
        if self.tuplecheck is True:
            for ini, allk in enumerate(self.iterable_list):
                for ini2 in range(len(allk[-1])):
                    keydi = allk[3][:ini2]
                    vari = get_from_original_iter(iterable=self.iterable, keys=keydi)
                    if isinstance(vari, tuple):
                        set_in_original_iter(
                            iterable=self.iterable, keys=keydi, value=list(vari)
                        )

            self.get_iterable_list()

        for origwert, lastkey, who, allkeys in self.iterable_list:
            strforlam2 = f"""self.iterable{'[' + ']['.join([str(f'"{x}"') if isinstance(x, str) else str(x) for x in allkeys]) + ']'} """
            originalvalue = str(who.__getitem__(lastkey))
            self.iterable_flat[allkeys] = {
                "get_value": NamedFunction(
                    name=partial(return_string, f"{originalvalue}"),
                    execute_function=partial(who.__getitem__, lastkey),
                    name_function=partial(who.__getitem__, lastkey),
                    str_prefix=f"Current value in {strforlam2}: ",
                    str_suffix="",
                ),
                "set_value": NamedFunction(
                    name=partial(return_string, f"Will access: {strforlam2}"),
                    execute_function=partial(who.__setitem__, lastkey),
                    name_function=partial(return_string, f"Will access: {strforlam2}"),
                ),
                "original": NamedFunction(
                    name=partial(return_string, f"{originalvalue}"),
                    execute_function=partial(return_string, f"{originalvalue}"),
                    name_function=partial(return_string, f"{originalvalue}"),
                ),
            }
