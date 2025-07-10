from openpyxl import Workbook
def EXCEL():
    start = datetime.strptime("2025-05-12", "%Y-%m-%d").date()
    week, value = 1, []

    while start <= date.today():
        end = min(start + timedelta(days=6), date.today())
        cursor.execute("SHOW COLUMNS FROM DailyTimeSheet")
        column = [i[0] for i in cursor.fetchall()]

        average = ",".join([f"ROUND(AVG({column[i]}),0)" for i in range(2, 17) if i not in (13, 14)])

        sql = f"select {average} from DailyTimeSheet where DAILY_DATE between %s and %s"
        cursor.execute(sql, [start, end])

        final = [f"WEEK-{week}", "---"] + [i for i in cursor.fetchone()]
        final[13:13] = ["----------", "---"]
        value.append(final)

        start += timedelta(days=7)
        week += 1

    # Print as table in console
    print(tabulate(value, headers=["DATE", "DAY", "MED", "GYM", "COM", "API", "MYSQL", "B1", "B2", "B3", "PYTHON", "TODO", "BOOK", "TASK", "HOURS", "OFFICE", "OVERALL"], tablefmt="pretty"))

    # === Export to Excel ===
    wb = Workbook()
    ws = wb.active
    ws.title = "Weekly Summary"

    # Write headers
    headers = ["DATE", "DAY", "MED", "GYM", "COM", "API", "MYSQL", "B1", "B2", "B3", "PYTHON", "TODO", "BOOK", "TASK", "HOURS", "OFFICE", "OVERALL"]
    ws.append(headers)

    # Write data rows
    for row in value:
        ws.append(row)

    # Save the Excel file
    wb.save(r"E:\FIRST PROJECT\Weekly_Summary.xlsx")
    print("\nExcel file 'Weekly_Summary.xlsx' created successfully!")

##WeekDisplay()





from datetime import datetime, timedelta, date
from tabulate import tabulate

def WeekDisplay():
    start = datetime.strptime("2025-05-12", "%Y-%m-%d").date()
    week, value, all_weeks_data = 1, [], []

    while start <= date.today():
        end = min(start + timedelta(days=6), date.today())

        # Get column names
        cursor.execute("SHOW COLUMNS FROM DailyTimeSheet")
        columns = [i[0] for i in cursor.fetchall()]

        # Prepare AVG columns (skip columns 13 and 14)
        avg_columns = ",".join([f"ROUND(AVG({columns[i]}), 0)" for i in range(2, 17) if i not in (13, 14)])

        # SQL Query
        sql = f"SELECT {avg_columns} FROM DailyTimeSheet WHERE DAILY_DATE BETWEEN %s AND %s"
        cursor.execute(sql, [start, end])

        row = cursor.fetchone()
        all_weeks_data.append(list(row))

        # Prepare final weekly row
        final = [f"WEEK-{week}", "---"] + list(row)
        final[13:13] = ["----------", "---"]  # Insert separator columns (TASK, HOURS)
        value.append(final)

        start += timedelta(days=7)
        week += 1
    print(all_weeks_data)
    print(value)
    # Calculate Week-to-Week % Change for all columns (MED to OVERALL)
    performance_rows = []
    for i in range(1, len(all_weeks_data)):
        prev_week = all_weeks_data[i - 1]
        curr_week = all_weeks_data[i]
        perf_row = [""] * len(value[0])

        # First column → W1-W2, W2-W3, etc.
        perf_row[0] = f"W{i}-W{i+1}"

        data_pos = 2  # Data starts from MED (column index 2 in display)
        for col_index in range(len(prev_week)):
            # Skip separator columns positions (TASK and HOURS at display position 13 and 14)
            insert_pos = data_pos if data_pos < 13 else data_pos + 2  # Adjust for separators

            if insert_pos >= len(perf_row):
                continue  # Safety check

            prev_value = prev_week[col_index]
            curr_value = curr_week[col_index]

            if prev_value not in (0, None):
                change = ((curr_value - prev_value) / prev_value) * 100
                perf_row[insert_pos] = f" {change:.0f}%"
            else:
                perf_row[insert_pos] = "N/A"

            data_pos += 1

        performance_rows.append(perf_row)

    # Merge weekly rows and performance rows
    final_output = []
    for i in range(len(value)):
        final_output.append(value[i])
        if i >= 1:
            final_output.append(performance_rows[i - 1])

    # Headers
    headers = ["DATE", "DAY", "MED", "GYM", "COM", "API", "MYSQL", "B1", "B2", "B3", "PYTHON", "TODO", "BOOK", "TASK", "HOURS", "OFFICE", "OVERALL"]

    # Print final table
    print(tabulate(final_output, headers=headers, tablefmt="pretty"))

##WeekDisplay()







