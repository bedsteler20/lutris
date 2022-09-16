import os
from lutris.gui.widgets.gi_composites import GtkTemplate
from lutris.util import datapath
from gi.repository import Gtk


@GtkTemplate(ui=os.path.join(datapath.get(), "ui", "game_art.ui"))
class ArtPickerDialog(Gtk.Dialog):
    """"""
    __gtype_name__ = "ArtPickerDialog"
    ArtPickerDialog = GtkTemplate.Child()
    def __init__(self) -> None:
        super().__init__()
        self.init_template()
        self.set_default_size(600, 600)
        self.show()
        self.ArtPickerDialog.s
        
    