from Collumns.disaster_subgroup import func_disasterSubgroup
from Collumns.continent import func_continent
from Collumns.date import func_date
from Collumns.disaster_subgroup import func_disasterSubgroup
from Collumns.disaster_type import func_disasterType
from Collumns.country import func_country
from Collumns.region import func_region
from Collumns.disaster_subtype import func_disasterSubtype

ch = int(input("Number of collumn? (0-6): "))


match ch:
    case 0:
        fst = func_date()
        print(fst)
    case 1:
        snd = func_disasterSubgroup()
        print(snd)
    case 2:
        trd = func_disasterType()
        print(trd)
    case 3:
        fth = func_disasterSubtype()
        print(fth)
    case 4:
        fith = func_country()
        print(fith)
    case 5:
        sth = func_region()
        print(sth)
    case 6:
        sevth = func_continent()
        print(sevth)
    case _:
        print("OHH NO")