def add_years_months(x: str) -> int:
    years_months = x.split()
    years = int(years_months[0].strip('yrs')) 
    months = int(years_months[1].strip('mon'))
    return years * 12 + months
