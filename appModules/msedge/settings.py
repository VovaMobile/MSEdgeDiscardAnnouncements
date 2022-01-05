from collections import namedtuple

Settings = namedtuple("Settings", "configKey, label, defaultValue")
settingItems = [
    Settings("PageLoading", _("Announce loading of pages"), "boolean(default=false)"),
    Settings("RefreshingPage", _("Announce page refresh"), "boolean(default=false)"),
    Settings("ClosingTab", _("Announce closing of tab"), "boolean(default=false)"),
    Settings("OpeningNewTab", _("Announce Opening of new tab"), "boolean(default=false)"),
    Settings("OpeningWindow", _("Announce window opening"), "boolean(default=false)"),
    Settings("HubDownloadsNewDownload", _("Announce starting file download"), "boolean(default=true)"),
    Settings("HubDownloadsCompleteState", _("Announce download completion"), "boolean(default=true)"),
    Settings("GoingBack", _("Announce navigating back"), "boolean(default=false)"),
    Settings("ToolbarButtonRemoved", _("Announce removing toolbar buttons"), "boolean(default=false)"),
    Settings("SearchMode", _("Announce of search mode"), "boolean(default=false)"),
    Settings("SearchModeAvailable", _("Announce availability of search mode"), "boolean(default=false)")
]
