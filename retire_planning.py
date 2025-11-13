# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 20:31:04 2025

@author: zheng
"""

from retirement import zunit, zrate, retire_plan
import matplotlib.pyplot as plt
            
# header  
si = zunit()
rate = zrate()
retire = retire_plan()

# jane_retirement_age     = 55   
# zheng_retirement_age    = 58   
# jane_403b_trigger_age  =  60  # > 59 1/2 year old
# zheng_401k_trigger_age =  60  # > 59 1/2 year old


# jane_retirement_year    = 2032  # work half-time or use saving
# zheng_retirement_year   = 2033  # work half-time or use saving
# jane_403b_trigger_year  = 2034  # > 59 1/2 year old
# zheng_401k_trigger_year = 2033  # > 59 1/2 year old
# pension_trigger_year    = 2036
# ss_trigger_year         = 2034

# retire.retire_plan_by_year(jane_retirement_year = 2032, 
#                            zheng_retirement_year = 2033, \
#                            jane_403b_trigger_year = 2034, \
#                            zheng_401k_trigger_year = 2033, \
#                            pension_trigger_year = 2036, \
#                            ss_trigger_year = 2034)
    
    
retire.retire_plan_by_age(jane_retirement_age = 55, 
                          zheng_retirement_age = 58, \
                          jane_403b_trigger_age = 60, \
                          zheng_401k_trigger_age = 60, \
                          pension_trigger_age = 62, \
                          ss_trigger_age = 62)
    
retire.cash_today = 250*si.KUSD
retire.calculate_retirement_expense(100000, fixed = False, print_flag = True)
retire.calculate_pension(2036, True)
retire.calculate_ssi(2034)
retire.calculate_401k(2032, 'lasting', print_flag='print')
retire.calculate_403b(2034, 'lasting', True)
retire.calculate_salary_income()
# retire.est_income_tax(89450,2024)
retire.calculate_cash_flow(True)
retire.export_to_spreadsheet()
