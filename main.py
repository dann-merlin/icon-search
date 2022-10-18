#/usr/bin/env python3

# Copyright (c) 2022 Merlin Sievers <merlin@sievvers.dev>
#
# This program is distributed under the terms of the GNU General Public License v3 (see COPYING)

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

fzf.prompt(choices=icons, fzf_options='--no-sort --exact')
