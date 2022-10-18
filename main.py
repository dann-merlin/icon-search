#/usr/bin/env python3

# Copyright (c) 2022 Merlin Sievers <merlin@sievvers.dev>
#
# This program is distributed under the terms of the GNU General Public License v3 (see COPYING)

import os

os.environ["DISPLAY"] = ":0"

from pyfzf.pyfzf import FzfPrompt

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

fzf = FzfPrompt()

gtk_icon_theme = Gtk.IconTheme.get_default()
icons = gtk_icon_theme.list_icons()
icons.sort(key=str.casefold)

for icon in icons:
    print(icon)

selected_name = fzf.prompt(choices=icons, fzf_options='--no-sort --exact')[0]

print(gtk_icon_theme.lookup_icon(selected_name, 256, 0).get_filename())
