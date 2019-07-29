import xlrd
import MySQLdb

# Open the workbook and define the worksheet
book = xlrd.open_workbook("pytest.xls")
sheet = book.sheet_by_name("source")

# Establish a MySQL connection
database = MySQLdb.connect (host="localhost", user = "root", passwd = "", db = "muster")

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

# Create the INSERT INTO sql query
query1 = """INSERT INTO Bank Details (branch_code, bank_pi_name, current_bank-po, po_branch_code, po_code_branch_name) VALUES (%s, %s, %s, %s, %s, %s)"""
query2 = """INSERT INTO accountdetails (reg_date, age_at_reg, current_account_no, account_no) VALUES (%s, %s, %s, %s)"""
query3 = """INSERT INTO paymentdetails (total_cash_payments, total_payment, status, worker_code, total_to_be_paid_for_muster, pending_payment_for_muster, ac_credited date) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
query4 = """INSERT INTO personaldetails (worker_name, worker_code, address, bpl_status, hoh_name, status, Village_Name, person_id, gender) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
query5 = """INSERT INTO Work (worker_code, no_day_work_muster, average_daily_wage, wagelist_no, job_card_number, travel_food_expenses) VALUES (%s, %s, %s, %s, %s, %s)"""


# Create a For loop to iterate through each row in the XLS file
for r in range(1, sheet.nrows):
    Village_Name = sheet.cell(r,).value
    ac_credited_date = sheet.cell(r,1).value
    acoount_no = sheet.cell(r,2).value
    address = sheet.cell(r,3).value
    age_at_reg = sheet.cell(r,4).value
    average_daily_wage = sheet.cell(r,5).value
    bank_pi_name = sheet.cell(r,6).value
    bpl_status = sheet.cell(r,7).value
    current_account_no = sheet.cell(r,8).value
    current_bank_po = sheet.cell(r,9).value
    gender	 = sheet.cell(r,10).value
    hoh_name	 = sheet.cell(r,11).value
    job_card_number = sheet.cell(r,12).value
    no_days_work_for_muster = sheet.cell(r, 13).value
    pending_payment_for_muster = sheet.cell(r, 14).value
    person_id = sheet.cell(r, 15).value
    po_branch_code = sheet.cell(r, 16).value
    po_code_branch_name = sheet.cell(r, 17).value
    reg_date = sheet.cell(r, 18).value
    status = sheet.cell(r, 19).value
    tool_payments = sheet.cell(r, 20).value
    total_cash_payments = sheet.cell(r, 21).value
    total_to_be_paid_for_muster = sheet.cell(r, 22).value
    travel_food_expenses = sheet.cell(r, 23).value
    wagelist_no = sheet.cell(r, 24).value
    worker_code = sheet.cell(r, 25).value
    worker_name = sheet.cell(r, 26).value

# Assign values from each row
    values1 = (branch_code, bank_pi_name, current_bank-po, po_branch_code, po_code_branch_name)
    values2 = (reg_date, age_at_reg, current_account_no, account_no)
    values3 = (total_cash_payments, total_payment, status, worker_code, total_to_be_paid_for_muster, pending_payment_for_muster, ac_credited_date)
    values4 = (worker_name, worker_code, address, bpl_status, hoh_name, status, Village_Name, person_id, gender)
    values5 = (worker_code, no_day_work_muster, average_daily_wage, wagelist_no, job_card_number, travel_food_expenses)
    # Execute sql Query
    cursor.execute(query1, values1)
    cursor.execute(query2, values2)
    cursor.execute(query3, values3)
    cursor.execute(query4, values4)
    cursor.execute(query5, values5)

# Close the cursor
cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()

# Print results
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print "imported  rows to MySQL!"
