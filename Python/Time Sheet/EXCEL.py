##from openpyxl import Workbook
##def EXCEL():
##    start = datetime.strptime("2025-05-12", "%Y-%m-%d").date()
##    week, value = 1, []
##
##    while start <= date.today():
##        end = min(start + timedelta(days=6), date.today())
##        cursor.execute("SHOW COLUMNS FROM DailyTimeSheet")
##        column = [i[0] for i in cursor.fetchall()]
##
##        average = ",".join([f"ROUND(AVG({column[i]}),0)" for i in range(2, 17) if i not in (13, 14)])
##
##        sql = f"select {average} from DailyTimeSheet where DAILY_DATE between %s and %s"
##        cursor.execute(sql, [start, end])
##
##        final = [f"WEEK-{week}", "---"] + [i for i in cursor.fetchone()]
##        final[13:13] = ["----------", "---"]
##        value.append(final)
##
##        start += timedelta(days=7)
##        week += 1
##
##    # Print as table in console
##    print(tabulate(value, headers=["DATE", "DAY", "MED", "GYM", "COM", "API", "MYSQL", "B1", "B2", "B3", "PYTHON", "TODO", "BOOK", "TASK", "HOURS", "OFFICE", "OVERALL"], tablefmt="pretty"))
##
##    # === Export to Excel ===
##    wb = Workbook()
##    ws = wb.active
##    ws.title = "Weekly Summary"
##
##    # Write headers
##    headers = ["DATE", "DAY", "MED", "GYM", "COM", "API", "MYSQL", "B1", "B2", "B3", "PYTHON", "TODO", "BOOK", "TASK", "HOURS", "OFFICE", "OVERALL"]
##    ws.append(headers)
##
##    # Write data rows
##    for row in value:
##        ws.append(row)
##
##    # Save the Excel file
##    wb.save(r"E:\FIRST PROJECT\Weekly_Summary.xlsx")
##    print("\nExcel file 'Weekly_Summary.xlsx' created successfully!")
##
####WeekDisplay()
##
##
##
##
##
##from datetime import datetime, timedelta, date
##from tabulate import tabulate
##
##def WeekDisplay():
##    start = datetime.strptime("2025-05-12", "%Y-%m-%d").date()
##    week, value, all_weeks_data = 1, [], []
##
##    while start <= date.today():
##        end = min(start + timedelta(days=6), date.today())
##
##        # Get column names
##        cursor.execute("SHOW COLUMNS FROM DailyTimeSheet")
##        columns = [i[0] for i in cursor.fetchall()]
##
##        # Prepare AVG columns (skip columns 13 and 14)
##        avg_columns = ",".join([f"ROUND(AVG({columns[i]}), 0)" for i in range(2, 17) if i not in (13, 14)])
##
##        # SQL Query
##        sql = f"SELECT {avg_columns} FROM DailyTimeSheet WHERE DAILY_DATE BETWEEN %s AND %s"
##        cursor.execute(sql, [start, end])
##
##        row = cursor.fetchone()
##        all_weeks_data.append(list(row))
##
##        # Prepare final weekly row
##        final = [f"WEEK-{week}", "---"] + list(row)
##        final[13:13] = ["----------", "---"]  # Insert separator columns (TASK, HOURS)
##        value.append(final)
##
##        start += timedelta(days=7)
##        week += 1
##    print(all_weeks_data)
##    print(value)
##    # Calculate Week-to-Week % Change for all columns (MED to OVERALL)
##    performance_rows = []
##    for i in range(1, len(all_weeks_data)):
##        prev_week = all_weeks_data[i - 1]
##        curr_week = all_weeks_data[i]
##        perf_row = [""] * len(value[0])
##
##        # First column → W1-W2, W2-W3, etc.
##        perf_row[0] = f"W{i}-W{i+1}"
##
##        data_pos = 2  # Data starts from MED (column index 2 in display)
##        for col_index in range(len(prev_week)):
##            # Skip separator columns positions (TASK and HOURS at display position 13 and 14)
##            insert_pos = data_pos if data_pos < 13 else data_pos + 2  # Adjust for separators
##
##            if insert_pos >= len(perf_row):
##                continue  # Safety check
##
##            prev_value = prev_week[col_index]
##            curr_value = curr_week[col_index]
##
##            if prev_value not in (0, None):
##                change = ((curr_value - prev_value) / prev_value) * 100
##                perf_row[insert_pos] = f" {change:.0f}%"
##            else:
##                perf_row[insert_pos] = "N/A"
##
##            data_pos += 1
##
##        performance_rows.append(perf_row)
##
##    # Merge weekly rows and performance rows
##    final_output = []
##    for i in range(len(value)):
##        final_output.append(value[i])
##        if i >= 1:
##            final_output.append(performance_rows[i - 1])
##
##    # Headers
##    headers = ["DATE", "DAY", "MED", "GYM", "COM", "API", "MYSQL", "B1", "B2", "B3", "PYTHON", "TODO", "BOOK", "TASK", "HOURS", "OFFICE", "OVERALL"]
##
##    # Print final table
##    print(tabulate(final_output, headers=headers, tablefmt="pretty"))
##
####WeekDisplay()
##
##
##
##




##
##import pandas as pd
##import mysql.connector
##
### 1. Read Excel File (Skip first row with "DATA")
##file_path = r"E:\SUSMITHA 2025\DevOps\Daily Time Sheet\EXCEL.xlsx"
##df = pd.read_excel(file_path, skiprows=1)  # 👈 Skipping the first row
##
### 2. Connect to MySQL
##conn = mysql.connector.connect(
##    host="localhost",
##    user="root",
##    password="Susmitha@789",
##    database="Daily_Time_Sheet_2025"
##)
##cursor = conn.cursor()
##
### 3. Insert Data
##for _, row in df.iterrows():
##    cursor.execute(
##        "INSERT INTO time_sheet (A, B, C) VALUES (%s, %s, %s)",
##        (int(row['A']), int(row['B']), int(row['C']))
##    )
##
### 4. Save and Close
##conn.commit()
##cursor.close()
##conn.close()
##
##print("✅ Excel data inserted into MySQL successfully!")

##
##import pandas as pd
##import mysql.connector
##
### 1. Read Excel and skip header rows
##file_path = r"E:\SUSMITHA 2025\DevOps\Daily Time Sheet\EXCEL.xlsx"
##df = pd.read_excel(file_path, skiprows=2)  # Skip the top 2 rows ("DATA", column headers)
##
### Optional: set proper column names if needed
##df.columns = [
##    'DAILY_DATE', 'DAILY_DAY', 'MEDITATION', 'GYM_WORKOUT', 'PYTHON_MYSQL',
##    'BLOCK_1', 'BLOCK_2', 'BLOCK_3', 'BLOCK_4', 'DEVOPS',  # DEVOPS will be ignored (it's calculated)
##    'MOTIVATION', 'BOOK_READING', 'REVIEW', 'TASK', 'HOURS'
##]
##
### Drop the 'DEVOPS' column if it exists, since it's calculated in MySQL
##if 'DEVOPS' in df.columns:
##    df = df.drop(columns=['DEVOPS'])
##
### 2. Connect to MySQL
##conn = mysql.connector.connect(
##    host="localhost",
##    user="root",
##    password="Susmitha@789",
##    database="Daily_Time_Sheet_2025"
##)
##cursor = conn.cursor()
##
### 3. Insert data row-by-row
##for i, row in df.iterrows():
##    try:
##        # Convert date from '7-Jul' to full date
##        date_val = pd.to_datetime(str(row['DAILY_DATE']) + '-2025').date()
##
##        cursor.execute("""
##            INSERT INTO time_sheet (
##                DAILY_DATE, MEDITATION, GYM_WORKOUT, PYTHON_MYSQL,
##                BLOCK_1, BLOCK_2, BLOCK_3, BLOCK_4,
##                MOTIVATION, BOOK_READING, REVIEW,
##                TASK, HOURS
##            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
##        """, (
##            date_val,
##            int(row['MEDITATION'] or 0),
##            int(row['GYM_WORKOUT'] or 0),
##            int(row['PYTHON_MYSQL'] or 0),
##            int(row['BLOCK_1'] or 0),
##            int(row['BLOCK_2'] or 0),
##            int(row['BLOCK_3'] or 0),
##            int(row['BLOCK_4'] or 0),
##            int(row['MOTIVATION'] or 0),
##            int(row['BOOK_READING'] or 0),
##            int(row['REVIEW'] or 0),
##            str(row['TASK']) if pd.notna(row['TASK']) else '----------',
##            float(row['HOURS'] or 0)
##        ))
##    except Exception as e:
##        print(f"❌ Error in row {i+2}: {e}")
##
### 4. Commit & Close
##conn.commit()
##cursor.close()
##conn.close()
##
##print("✅ Excel data inserted into `time_sheet` table successfully!")
##



##import pandas as pd
##
### Excel file path
##file_path = r"E:\SUSMITHA 2025\DevOps\Daily Time Sheet\EXCEL.xlsx"
##
### Step 1: Read the sheet, skip first 3 rows (no headers)
##df = pd.read_excel(file_path, skiprows=3, header=None)
##
### Step 2: Define required columns
##columns_to_display = [0, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
##
### Step 3: Loop and display only valid rows
##print("📅 Parsed Dates with Selected Column Values:")
##for i, row in df.iterrows():
##    row_number = i + 4  # Actual Excel row number for visual tracking
##
##    # Skip every 8th row (e.g., 8th, 16th, etc.)
##    print(i)
##    if (i + 1) % 8 == 0:
##        continue
##
##    try:
##        # Get selected columns
##        selected_values = [row[col] for col in columns_to_display]
##
##        # Skip row if any selected value is NaN
##        if any(pd.isna(val) for val in selected_values):
##            continue
##
##        # Convert first column (like '13-Jul') to full 2025 date
##        raw_date = str(selected_values[0])
##        parsed_date = pd.to_datetime(raw_date + "-2025" if '-' in raw_date else raw_date).date()
##        selected_values[0] = parsed_date
##
##        # Print the row
##        print(f"Row {row_number}: {selected_values}")
##    except Exception as e:
##        print(f"❌ Error in row {row_number}: {e}")


##
##import pandas as pd
##import mysql.connector
##
### Excel file path
##file_path = r"E:\SUSMITHA 2025\DevOps\Daily Time Sheet\Daily Time Sheet.xlsx"
##
##df = pd.read_excel(file_path, sheet_name="8 Months", skiprows=3, header=None)
##
##
### Columns to use [0 = Date, 2 = MEDITATION, ..., 12 = REVIEW]
##columns_to_use = [0, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12,15]
##
### Step 2: Connect to MySQL
##conn = mysql.connector.connect(
##    host="localhost",
##    user="root",
##    password="Susmitha@789",
##    database="Daily_Time_Sheet_2025"
##)
##cursor = conn.cursor()
##
### Step 3: Loop and insert valid records
##print("📥 Inserting into MySQL:")
##for i, row in df.iterrows():
##    row_number = i + 4
##
##    if (i + 1) % 8 == 0:
##        continue  # Skip every 8th row
##
##    try:
##        selected = [row[col] for col in columns_to_use]
##        selected = [0 if pd.isna(val) else val for val in selected]
##        # Prepare values
##        parsed_date = pd.to_datetime(str(selected[0]) + "-2025").date()
##        meditation = int(selected[1])
##        gym = int(selected[2])
##        python = int(selected[3])
##        b1 = int(selected[4])
##        b2 = int(selected[5])
##        b3 = int(selected[6])
##        b4 = int(selected[7])
##        moti = int(selected[8])
##        book = int(selected[9])
##        review = int(selected[10])
##        task = str(row[13]) if pd.notna(row[13]) else '----------'
##        hours = float(row[14]) if pd.notna(row[14]) else 0.0
##        OFFICE_OTHER=int(selected[10])
##        #OFFICE_OTHER = int(selected[10]) if pd.notna(selected[10]) else 0
##
##        # Insert
##        cursor.execute("""
##            INSERT INTO time_sheet (
##                DAILY_DATE, MEDITATION, GYM_WORKOUT, PYTHON_MYSQL,
##                BLOCK_1, BLOCK_2, BLOCK_3, BLOCK_4,
##                MOTIVATION, BOOK_READING, REVIEW,
##                TASK, HOURS,OFFICE_OTHER
##            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
##        """, (
##            parsed_date, meditation, gym, python,
##            b1, b2, b3, b4,
##            moti, book, review,
##            task, hours,OFFICE_OTHER
##        ))
##
##        print(f"✅ Row {row_number} inserted: {parsed_date}")
##
##    except Exception as e:
##        print(f"❌ Row {row_number} failed: {e}")
##
### Finalize
##conn.commit()
##cursor.close()
##conn.close()
##
##print("✅ All data inserted into `time_sheet` table successfully.")



##import pandas as pd
##import mysql.connector
##
### Excel file path
##file_path = r"E:\SUSMITHA 2025\DevOps\Daily Time Sheet\Daily Time Sheet.xlsx"
##
### Read the Excel sheet (skip 3 header rows)
##df = pd.read_excel(file_path, sheet_name="8 Months", skiprows=3, header=None)
##
### Columns to use [0 = Date, 2 = MEDITATION, ..., 12 = REVIEW, 15 = OFFICE_OTHER]
##columns_to_use = [0, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 15]
##
### Connect to MySQL
##conn = mysql.connector.connect(
##    host="localhost",
##    user="root",
##    password="Susmitha@789",
##    database="Daily_Time_Sheet_2025"
##)
##cursor = conn.cursor()
##
##print("📥 Inserting or Updating into MySQL:")
##for i, row in df.iterrows():
##    row_number = i + 4
##
##    if (i + 1) % 8 == 0:
##        continue  # Skip every 8th row (merged row)
##
##    try:
##        selected = [row[col] for col in columns_to_use]
##        selected = [0 if pd.isna(val) else val for val in selected]
##
##        # Parse date
##        parsed_date = pd.to_datetime(str(selected[0]) + "-2025").date()
##
##        # Extract values
##        meditation = int(selected[1])
##        gym = int(selected[2])
##        python = int(selected[3])
##        b1 = int(selected[4])
##        b2 = int(selected[5])
##        b3 = int(selected[6])
##        b4 = int(selected[7])
##        moti = int(selected[8])
##        book = int(selected[9])
##        review = int(selected[10])
##        OFFICE_OTHER = int(selected[11])
##
##        task = str(row[13]) if pd.notna(row[13]) else '----------'
##        hours = float(row[14]) if pd.notna(row[14]) else 0.0
##
##        # Insert or Update
##        cursor.execute("""
##            INSERT INTO time_sheet (
##                DAILY_DATE, MEDITATION, GYM_WORKOUT, PYTHON_MYSQL,
##                BLOCK_1, BLOCK_2, BLOCK_3, BLOCK_4,
##                MOTIVATION, BOOK_READING, REVIEW,
##                TASK, HOURS, OFFICE_OTHER
##            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
##            ON DUPLICATE KEY UPDATE
##                MEDITATION = VALUES(MEDITATION),
##                GYM_WORKOUT = VALUES(GYM_WORKOUT),
##                PYTHON_MYSQL = VALUES(PYTHON_MYSQL),
##                BLOCK_1 = VALUES(BLOCK_1),
##                BLOCK_2 = VALUES(BLOCK_2),
##                BLOCK_3 = VALUES(BLOCK_3),
##                BLOCK_4 = VALUES(BLOCK_4),
##                MOTIVATION = VALUES(MOTIVATION),
##                BOOK_READING = VALUES(BOOK_READING),
##                REVIEW = VALUES(REVIEW),
##                TASK = VALUES(TASK),
##                HOURS = VALUES(HOURS),
##                OFFICE_OTHER = VALUES(OFFICE_OTHER)
##        """, (
##            parsed_date, meditation, gym, python,
##            b1, b2, b3, b4,
##            moti, book, review,
##            task, hours, OFFICE_OTHER
##        ))
##
##        print(f"✅ Row {row_number} inserted/updated: {parsed_date}")
##
##    except Exception as e:
##        print(f"❌ Row {row_number} failed: {e}")
##
### Finalize
##conn.commit()
##cursor.close()
##conn.close()
##
##print("✅ All data inserted or updated into `time_sheet` table successfully.")



import pandas as pd
import mysql.connector
file_path = r"E:\SUSMITHA 2025\DevOps\Daily Time Sheet\Daily Time Sheet.xlsx"
df = pd.read_excel(file_path, sheet_name="8 Months", skiprows=3, header=None)
columns_to_use = [0, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 15]
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Susmitha@789",
    database="Daily_Time_Sheet_2025"
)
cursor = conn.cursor(dictionary=True)
db_columns = [
    "DAILY_DATE", "MEDITATION", "GYM_WORKOUT", "PYTHON_MYSQL",
    "BLOCK_1", "BLOCK_2", "BLOCK_3", "BLOCK_4",
    "MOTIVATION", "BOOK_READING", "REVIEW", "OFFICE_OTHER"
]
print("📥 Inserting or Updating into MySQL:")
for i, row in df.iterrows():
    row_number = i + 4
    if (i + 1) % 8 == 0:
        continue
    try:
        selected = [row[col] for col in columns_to_use]
        selected = [0 if pd.isna(val) else val for val in selected]
        parsed_date = pd.to_datetime(str(selected[0]) + "-2025").date()
        selected[0] = parsed_date  # Replace with full date
        cursor.execute("SELECT * FROM time_sheet WHERE DAILY_DATE = %s", (parsed_date,))
        existing = cursor.fetchone()
        if not existing:
            # New insert
            task = str(row[13]) if pd.notna(row[13]) else '----------'
            hours = float(row[14]) if pd.notna(row[14]) else 0.0
            cursor.execute(f"""INSERT INTO time_sheet ({", ".join(db_columns)},TASK, HOURS)
            VALUES ({", ".join(['%s'] * len(db_columns))}, %s, %s)""", tuple(selected) + (task, hours))
            print(f"🆕 Inserted ✅ Row {row_number}: {parsed_date}")
        else:
            updates = {}
            for j, col in enumerate(db_columns[1:]):  # Skip DAILY_DATE
                if int(existing[col]) != int(selected[j + 1]):
                    updates[col] = int(selected[j + 1])
            if updates:
                set_clause = ", ".join([f"{col} = %s" for col in updates])
                values = list(updates.values()) + [parsed_date]
                cursor.execute(f"UPDATE time_sheet SET {set_clause} WHERE DAILY_DATE = %s", values)
                print(f"🔁 Updated {len(updates)} field(s) ✅ Row {row_number}: {parsed_date}")
    except Exception as e:
        print(f"❌ Row {row_number} failed: {e}")
print("✅ All data synced with `time_sheet` table.")
conn.commit()
cursor.close()
conn.close()


























