import pandas as pd


# write not monitored vms onto the report
def write_not_monitored_vms(rvtools_name2ip, monitoring_name2ip, excel_writer):
    # write vm not under monitoring
    not_monitored_vms = []
    for vm_name in rvtools_name2ip:
        if not rvtools_name2ip[vm_name] in monitoring_name2ip.values():
            not_monitored_vms.append([vm_name, rvtools_name2ip[vm_name], ""])
    not_monitored_vms_df = pd.DataFrame(not_monitored_vms, columns=["VM", "IP Address", "H24 Monitoring"])

    not_monitored_vms_df.to_excel(
        excel_writer,
        sheet_name="VMs non monitorate",
        index=False)


# write vm in monitoring but not in rvtools
def write_vms_not_rvtools(rvtools_name2ip, monitoring_name2ip, excel_writer):
    not_rvtools_vms = []
    for vm_name in monitoring_name2ip:
        if not monitoring_name2ip[vm_name] in rvtools_name2ip.values():
            not_rvtools_vms.append([vm_name, monitoring_name2ip[vm_name]])

    pd.DataFrame(not_rvtools_vms, columns=["VM", "IP Address"]).to_excel(
        excel_writer,
        sheet_name="VMs monitorate non in RVTools",
        index=False)
