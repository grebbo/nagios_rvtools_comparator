import pandas as pd
from argument_parser import parse_args
import report_functions

# parse command line args
args = parse_args()

with pd.ExcelWriter("res/" + "Report confronto " + args["name"] + ".xlsx") as excel_writer:
    # import files to compare: monitoring (status sheet) and rvtools (network)
    monitoring_file = pd.read_excel(args["monitoring"], sheet_name="Status")
    rvtools_file = pd.read_excel(args["rvtools"], sheet_name="vNetwork", na_values="unknown").\
        dropna(subset=["IP Address"])

    # pick each vm with its ip address in rvtools
    rvtools_name_ip = dict(zip(list(rvtools_file["VM"]), [list(filter(
        lambda single_ip: ("." in single_ip), ip_list.replace(" ", "").split(",")))[0]
                                                            for ip_list in list(rvtools_file["IP Address"])]))

    # pick each vm with its ip address in monitoring
    monitoring_name_ip = dict(zip(list(monitoring_file["Hostname"]), list(monitoring_file["IP"])))

    # write not monitored vms onto the report
    report_functions.write_not_monitored_vms(
        rvtools_name2ip=rvtools_name_ip,
        monitoring_name2ip=monitoring_name_ip,
        excel_writer=excel_writer)

    # write vm in monitoring but not in rvtools
    report_functions.write_vms_not_rvtools(
        rvtools_name2ip=rvtools_name_ip,
        monitoring_name2ip=monitoring_name_ip,
        excel_writer=excel_writer)
