#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import subprocess


def _get_node_stats_str(node):
    df = subprocess.Popen(["df", node.path], stdout=subprocess.PIPE)
    output = df.communicate()[0]

    output = output.split("\n")
    if len(output) < 2:
        return "Unable to parse the output of the `df` command"

    output = output[1].split()
    if len(output) < 6:
        return "Invalid data format returned by the `df` command"

    used, available, percent = output[2:-1]

    return "{0} / {1} ({2})".format(available, used, percent)


def register_plugin(manager):
    manager.register_widget(
        place='header',
        type='span',
        text=lambda x: _get_node_stats_str(x),
    )
