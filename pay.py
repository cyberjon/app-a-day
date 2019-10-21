hours_worked = 39
over_time_hours = 39




standar_pay_rate = hours_worked*35
over_time_pay_rate = over_time_hours *50 
gross_pay = (standar_pay_rate + over_time_pay_rate) *12

if gross_pay > 0 and gross_pay < 18000:
    net_pay = gross_pay

    print(f'Hours Worked         :       {hours_worked}')
    print(f'Standard pay amount  :       {standar_pay_rate}')
    print(f'Over-time pay amount  :       {over_time_pay_rate}')
    print(f'Gross Pay            :       {gross_pay}')
    print('-------------------------------------')
    print(f'Total Tax            :       {""}')
    print('-------------------------------------')
    print(f'Net Pay              :       {net_pay}')

elif gross_pay > 18000:
    tax_21 = (gross_pay-1800)*0.21
    net_pay =gross_pay+tax_21

    print(f'Hours Worked         :       {hours_worked}')
    print(f'Standard pay amount  :       {standar_pay_rate}')
    print(f'Over-time pay amount  :       {over_time_pay_rate}')
    print(f'Gross Pay            :       {gross_pay}')
    print('-------------------------------------')
    print(f'Total Tax            :       {round(tax_21)}')
    print('-------------------------------------')
    print(f'Net Pay              :       {net_pay}')

elif gross_pay > 49000:
    tax_42 = (gross_pay-49800)*0.42
    net_pay =gross_pay+tax_42

    print(f'Hours Worked         :       {hours_worked}')
    print(f'Standard pay amount  :       {standar_pay_rate}')
    print(f'Over-time pay amount  :       {over_time_pay_rate}')
    print(f'Gross Pay            :       {gross_pay}')
    print('-------------------------------------')
    print(f'Total Tax            :       {round(tax_42)}')
    print('-------------------------------------')
    print(f'Net Pay              :       {net_pay}')