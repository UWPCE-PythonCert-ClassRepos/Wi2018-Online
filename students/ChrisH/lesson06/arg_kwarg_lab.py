#!/usr/bin/env python3
# -----------------------------------------------------------
# arg_kwarg_lab.py
#  https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/args_kwargs.html
# -----------------------------------------------------------


def func(fore_color='black', back_color='white', link_color='green', visited_color='gray'):
    return (fore_color, back_color, link_color, visited_color)

def newfunc(*args, **kwargs):
    colors = (['fore_color', 'black'],
              ['back_color', 'white'],
              ['link_color', 'green'],
              ['visited_color', 'gray'])

    print("args:", args)
    for index, arg in enumerate(args):
        colors[index][1] = arg

    print('kwargs:', kwargs)

    used_options = [kw[0] for kw in colors[:len(args)]]
    print("positional args used:", used_options)
    print("keyword args used:", list(kwargs.keys()))

    for kw, arg in kwargs.items():
        if kw in used_options:
            raise TypeError('Keyword argument already used by positional argument.')
        else:
            for item in colors:
                if item[0] == kw:
                    item[1] = arg


    return tuple([item[-1] for item in colors])


if __name__ == '__main__':

    pass
