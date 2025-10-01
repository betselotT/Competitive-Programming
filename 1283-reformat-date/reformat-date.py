class Solution:
    def reformatDate(self, date: str) -> str:
        # Remove the suffix from the day
        day = date.split()[0][:-2]  # This removes the last two characters (the suffix)
        month = date.split()[1]
        year = date.split()[2]
        # Create a mapping from month abbreviation to month number
        month_mapping = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sep": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12"
        }
        
        # Format the date into YYYY-MM-DD
        formatted_date = f"{year}-{month_mapping[month]}-{int(day):02d}"
        return formatted_date