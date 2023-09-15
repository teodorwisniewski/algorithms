from dataclasses import dataclass


class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []



def createCompanyStructure():
    # Create OrgChart objects based on the input structure

    report_1 = OrgChart("E")
    report_2 = OrgChart("I")
    nodes = {
        "A": OrgChart("A"),
        "B": OrgChart("B"),
        "C": OrgChart("C"),
        "D": OrgChart("D"),
        "E": report_1,
        "F": OrgChart("F"),
        "G": OrgChart("G"),
        "H": OrgChart("H"),
        "I": report_2
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

    return nodes["A"], report_1, report_2





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


@dataclass
class OrgInfo:
    lowest_common_menago: str
    num_of_reports: int


def getLowestCommonManager(topManager, reportOne, reportTwo):
    # Write your code here.
    return getOrgInfo(topManager, reportOne, reportTwo).lowest_common_menago


def getOrgInfo(manager: OrgChart, reportOne: OrgChart, reportTwo: OrgChart) -> OrgInfo:

    num_of_reports = 0
    for direct_report in manager.directReports:
        org_info = getOrgInfo(direct_report, reportOne, reportTwo)
        if org_info.lowest_common_menago is not None:
            return org_info
        num_of_reports += org_info.num_of_reports
    
    if manager in {reportOne, reportTwo}:
        num_of_reports += 1

    if num_of_reports == 2:
        return OrgInfo(manager, num_of_reports)
    else:
        return OrgInfo(None, num_of_reports)


top_manager, report_1, report_2 = createCompanyStructure()

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

res = getLowestCommonManager(top_manager, report_1, report_2)
print(f"getLowestCommonManager {res.name}")






