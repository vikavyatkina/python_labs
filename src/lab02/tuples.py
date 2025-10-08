def format_record(rec: tuple[str, str, float]) -> str:
    if any(str(x)=='' for x in rec):
        return 'ValueError'

    fio=str(rec[0]).split()
    group=str(rec[1])
    gpa=f'{float(rec[2]):.2f}'
    fio1=''
    fam=0 

    for i in range(len(fio)):
        if fio[i]!='' and fam==0:
            first_let=str(fio[i])[0].upper() 
            fio1+=first_let+str(fio[i][1:])+' '
            fam=1
        elif fio[i]!='' and fam==1:
            first_let=str(fio[i])[0].upper()
            fio1 += first_let + '.'
    res=fio1+', гр. '+group+', GPA '+str(gpa)
    return res
r=("Иванов Иван Иванович", "BIVT-25", 4.6)
r2=("Петров Пётр", "IKBO-12", 5.0)
r3=("Петров Пётр Петрович", "IKBO-12", 5.0)
r4=("  сидорова  анна   сергеевна ", "ABB-01", 3.999)
print(format_record(r))
print(format_record(r2))
print(format_record(r3))
print(format_record(r4))