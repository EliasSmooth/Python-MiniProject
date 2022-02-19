#months dictionary used for extracting date values out of name identifiers
months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}

#Function searches through month array and returns the numerical value of a given month
def monthMatch(month):
        for i in months:
            if i == month:
                return (months[month])
            else: pass

