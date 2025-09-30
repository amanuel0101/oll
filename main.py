# list of pkg managers for each terminal ({os:{pkgm:{"search":"search_cmd", "install":"install_cmd", "uninstall":"uninstall_cmd"}})
pkgms = {}

def pkgm_has(pkgm, pkg):
    pass

def oll(os_, pkg):
    # if os(os_) is not yet implemented or is incorrect exit(1)
    if os_ not in pkgms:
        return 1

    # list of possible pkgms of the specific os(os_)
    loc_pkgms = pkgms[os_]

    # list of pkgms that have the pkg ["install_cmd"]
    availablein = []
    # loop through loc_pkgms and get all that have the pkg available then store them in availablein
    for i in loc_pkgms:
        x = pkgm_has(i, pkg)
        if x:
            loc_pkgms.append(x)

