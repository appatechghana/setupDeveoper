from postGreAddEditDeleteCls import identifiers, sheet

begin = 7
# p = begin
while True:
    begin = identifiers(begin,"a","e","d")
    # print begin
    if (sheet.cell(column=5, row=begin).value == None):
        break
