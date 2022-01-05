# MSEdgeDiscardAnnouncements: An appModule to discard some of notifications generated by Microsoft Edge
# Copyright (C) 2022 Beqa Gozalishvili
# Released under GPL 2

import appModuleHandler
import config
import gui
import wx
from .settings import settingItems
    
config.conf.spec["MSEdgeDiscardAnnouncements"] = {setting.configKey: setting.defaultValue for setting in settingItems}

class AppModule(appModuleHandler.AppModule):
    activityIDs = []

    def __init__(self, processID, appName):
        super().__init__(processID, appName)
        categoryClasses = gui.settingsDialogs.NVDASettingsDialog.categoryClasses
        if not (MSEdgeDiscardAnnouncementsPanel in categoryClasses):
            categoryClasses.append(MSEdgeDiscardAnnouncementsPanel)

    def terminate(self):
        super().terminate()
        gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(MSEdgeDiscardAnnouncementsPanel)

    def getActivityIDsFromConfig(self):
        edgeConf = config.conf["MSEdgeDiscardAnnouncements"]
        self.activityIDs = [k for k, v in edgeConf.items() if type(v) == bool and v == False]

    def event_appModule_gainFocus(self):
        self.getActivityIDsFromConfig()

    def event_UIA_notification(self, obj, nextHandler, activityId=None, **kwargs):
        if activityId in self.activityIDs: return
        nextHandler()

class MSEdgeDiscardAnnouncementsPanel(gui.settingsDialogs.SettingsPanel):
    title = "Microsoft Edge discard announcements"

    def makeSettings(self, sizer):
        self.config = config.conf["MSEdgeDiscardAnnouncements"]
        self.helper = gui.guiHelper.BoxSizerHelper(self, sizer=sizer)
        for setting in settingItems:
                widget = self.helper.addItem(wx.CheckBox(self, label=setting.label, name=setting.configKey))
                widget.SetValue(self.config[setting.configKey])

    def onSave(self):
        for child in self.helper.sizer.GetChildren():
            widget = child.GetWindow()
            if isinstance(widget, wx.CheckBox):
                self.config[widget.Name] = widget.IsChecked()
