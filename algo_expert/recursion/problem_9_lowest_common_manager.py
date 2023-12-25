from dataclasses import dataclass


class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []



def createCompanyStructure():
    # Create OrgChart objects based on the input structure
    nodes = {
        "A": OrgChart("A"),
        "B": OrgChart("B"),
        "C": OrgChart("C"),
        "D": OrgChart("D"),
        "E": OrgChart("E"),
        "F": OrgChart("F"),
        "G": OrgChart("G"),
        "H": OrgChart("H"),
        "I": OrgChart("I")
    }

    # Set up relationships based on the provided structure
    relationships = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F", "G"],
        "D": ["H", "I"]
    }
    
    for manager_name, report_names in relationships.items():
        for report_name in report_names:
            nodes[manager_name].directReports.append(nodes[report_name])

    return nodes["A"]





# TopManager
# |-- Manager1
# |   |-- Manager1.1
# |   |   |-- Employee1
# |   |   `-- Employee2
# |   `-- Manager1.2
# |       |-- Employee3
# |       `-- Employee4
# |-- Manager2
# |   `-- Manager2.1
# |       |-- Manager2.1.1
# |       |   |-- Employee5
# |       |   `-- Employee6
# |       `-- Manager2.1.2
# |           |-- Employee7
# |           `-- Employee8
# `-- Manager3
#     |-- Manager3.1
#     |   |-- Employee9
#     |   `-- Employee10
#     `-- Manager3.2
#         |-- Employee11
#         `-- Employee12






def getLowestCommonManager(topManager, reportOne, reportTwo):    
    res = getOrgInfo(topManager, reportOne, reportTwo)
    if res is not None:
        return res.lowest_common_manager
    return res


@dataclass
class OrgInfo:
    lowest_common_manager: OrgChart
    nb_searched_reports: int 


def getOrgInfo(manager, reportOne, reportTwo):

    num_searched_reports = 0
    for report in manager.directReports:
        org_info = getOrgInfo(report, reportOne, reportTwo)
        if org_info.lowest_common_manager is not None:
            return org_info
        num_searched_reports += org_info.nb_searched_reports
    if manager.name in [reportOne, reportTwo]:
        num_searched_reports += 1
    lowest_common_manager = manager if num_searched_reports == 2 else None
    return OrgInfo(lowest_common_manager, num_searched_reports)


# Create the company structure
top_manager = createCompanyStructure()


reportOne = "E"
reportTwo = "I"
topManagerName = "A"
top_manager = createCompanyStructure()

# A
# |-- B
# |   |-- D
# |   |   |-- H
# |   |   |-- I
# |   |-- E
# |
# |-- C
#     |-- F
#     |-- G

res = getLowestCommonManager(top_manager, reportOne, reportTwo)
print(f"getLowestCommonManager {res.name}")






