# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 21:30:00 2024

@author: Zheng Huang
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import math
from datetime import datetime


current_year = datetime.now().year

class zunit:
        USD = 1 # USD today
        MUSD = 1E6*USD
        KUSD = 1E3*USD
        day = 1
        yr = 365
        month = yr/day
        def __init__(self):
            pass
    
class zrate:
    inflation = 0.03 # per year
    standard_investment_return = 0.07 # per year
    jane_annual_salary_change  = 0.02
    zheng_annual_salary_change = 0.01
    annual_401k_contribution_limit_increase = 0.02
    zheng_401k_withdraw_rate = 0.04
    jane_403b_withdraw_rate  = 0.04
    state_tax_rate           = 0.050
    
    def __init__(self):
        print("inflation = {:,.1%}".format(self.inflation))
        print("standard_investment_return = {:,.1%}".format(self.standard_investment_return))
        # print("zheng_401k_withdraw_rate   = {:,.1%}".format(self.zheng_401k_withdraw_rate))
        # print("jane_403b_withdraw_rate    = {:,.1%}".format(self.jane_403b_withdraw_rate))
        print("--------------------------------------------------------------")
        
    def to_dollar_today(self, year):
        current_year = datetime.now().year
        conversion_rate = 1/(1+self.inflation)**(year-current_year)
        return conversion_rate
    
    def to_dollar_future(self, year):
        current_year = datetime.now().year
        conversion_rate = (1+self.inflation)**(year-current_year)
        return conversion_rate       
        

class retire_plan(zunit,zrate):
    jane_birth_year = 1974
    zheng_birth_year =  1972
    
    def __init__(self): 
        self.pre_retire_expense     = 0.0
        self.post_retire_expense    = 0.0
        self.small_property_expense = 0.0       

    
    def retire_plan_by_year(self, jane_retirement_year, zheng_retirement_year, \
                        jane_403b_trigger_year, zheng_401k_trigger_year, \
                        pension_trigger_year, ss_trigger_year):

        self.jane_retirement_year      = jane_retirement_year
        self.zheng_retirement_year     = zheng_retirement_year
        self.jane_403b_trigger_year    = jane_403b_trigger_year
        self.zheng_401k_trigger_year   = zheng_401k_trigger_year
        self.jane_pension_trigger_year = pension_trigger_year
        self.zheng_ss_trigger_year     = ss_trigger_year

        self.jane_retirement_age  = self.jane_retirement_year  - self.jane_birth_year
        self.zheng_retirement_age = self.zheng_retirement_year - self.zheng_birth_year
        
        self.jane_403b_trigger_age  = self.jane_403b_trigger_year - self.jane_birth_year
        self.zheng_401k_trigger_age = self.zheng_401k_trigger_year - self.zheng_birth_year
        
        self.jane_pension_trigger_age = self.jane_pension_trigger_year - self.jane_birth_year
        self.zheng_ss_trigger_age     = self.zheng_ss_trigger_year - self.zheng_birth_year        
        self.show_retire_age_summary()
        
    def retire_plan_by_age(self, jane_retirement_age, zheng_retirement_age, \
                       jane_403b_trigger_age, zheng_401k_trigger_age, \
                       pension_trigger_age, ss_trigger_age):        
        
        self.jane_retirement_age      = jane_retirement_age
        self.zheng_retirement_age     = zheng_retirement_age
        self.jane_403b_trigger_age    = jane_403b_trigger_age
        self.zheng_401k_trigger_age   = zheng_401k_trigger_age
        self.jane_pension_trigger_age = pension_trigger_age
        self.zheng_ss_trigger_age     = ss_trigger_age

        self.jane_retirement_year  = self.jane_retirement_age  + self.jane_birth_year
        self.zheng_retirement_year = self.zheng_retirement_age + self.zheng_birth_year
        
        self.jane_403b_trigger_year  = self.jane_403b_trigger_age + self.jane_birth_year
        self.zheng_401k_trigger_year = self.zheng_401k_trigger_age + self.zheng_birth_year
        
        self.jane_pension_trigger_year = self.jane_pension_trigger_age + self.jane_birth_year
        self.zheng_ss_trigger_year    = self.zheng_ss_trigger_age + self.zheng_birth_year
        self.show_retire_age_summary()

    def show_retire_age_summary(self):
        print("Jane retirement year     {:d}".format(self.jane_retirement_year)) 
        print("Jane age at retirement   {:d}".format(self.jane_retirement_age)) 
        print("Zheng retirement year    {:d}".format(self.zheng_retirement_year)) 
        print("Zheng age at retirement  {:d}".format(self.zheng_retirement_age)) 

        if (self.jane_403b_trigger_year-1974)<60:
            print("Panelty to withdraw 403b before 59.5 age!!")
            self.jane_403b_trigger_year = 1974 + 60
        print("Jane 403b trigger year   {:d}".format(self.jane_403b_trigger_year)) 
        print("Jane age at 403b trigger {:d}".format(self.jane_403b_trigger_age))
        
        if (self.zheng_401k_trigger_year-1972)<60:
            print("Panelty to withdraw 401k before 59.5 age!!")
            self.zheng_401k_trigger_year = 1972 + 60
        print("Zheng 401k trigger year  {:d}".format(self.zheng_401k_trigger_year)) 
        print("Zheng age 401k trigger   {:d}".format(self.zheng_401k_trigger_age)) 

        # no panelty 401k withdraw year
        if (self.jane_pension_trigger_year-1974)<55:
            print("Can't collect pension before 55 !!")
            self.pension_trigger_year = 1974 + 55
        print("Jane pension trigger       {:d}".format(self.jane_pension_trigger_year)) 
        print("Jane age pension triggered {:d}".format(self.jane_pension_trigger_age)) 
        if (self.zheng_ss_trigger_year-1972)<62:
            print("Can't collect social security before 62 !!")
            self.zheng_ss_trigger_year = 1972 + 62
        print("Zheng social security trigger year  {:d}".format(self.zheng_ss_trigger_year)) 
        print("Zheng age social security triggered {:d}".format(self.zheng_ss_trigger_age)) 
        
        self.jane_salary_today = 100*self.KUSD
        self.zheng_salary_today = 235*self.KUSD
        self.current_year = int(datetime.now().year)
        print("current year {:d}".format(self.current_year))

        self.cash_today = 300*self.KUSD
        crt_yr = self.current_year
        trk_to = 2070 
        track_range = np.linspace(crt_yr, trk_to, trk_to-crt_yr+1)
        self.track_range = track_range.astype(int)
        self.zheng_age          = np.zeros(trk_to-crt_yr+1)
        self.jane_age           = np.zeros(trk_to-crt_yr+1)
        self.zheng_401k_balance = np.zeros(trk_to-crt_yr+1)
        self.zheng_401k_IAB     = np.zeros(trk_to-crt_yr+1)
        self.zheng_401k_chipin  = np.zeros(trk_to-crt_yr+1)
        self.jane_403b_balance  = np.zeros(trk_to-crt_yr+1)
        self.jane_403b_chipin   = np.zeros(trk_to-crt_yr+1)
        self.jane_403b_IAB      = np.zeros(trk_to-crt_yr+1)
        self.zheng_job_income   = np.zeros(trk_to-crt_yr+1)
        self.jane_job_income    = np.zeros(trk_to-crt_yr+1)
        self.zheng_401k_withdraw= np.zeros(trk_to-crt_yr+1)
        self.jane_403b_withdraw = np.zeros(trk_to-crt_yr+1)
        self.ss_income          = np.zeros(trk_to-crt_yr+1)
        self.pension_income     = np.zeros(trk_to-crt_yr+1)
        self.expense            = np.zeros(trk_to-crt_yr+1)
        self.gross_income       = np.zeros(trk_to-crt_yr+1)
        self.income_after_tax   = np.zeros(trk_to-crt_yr+1)
        self.income_IAB         = np.zeros(trk_to-crt_yr+1)
        self.cash_burn          = np.zeros(trk_to-crt_yr+1)
        self.cash_position      = np.zeros(trk_to-crt_yr+1) 
        print("--------------------------------------------------------------")
        for i, iyr in enumerate(self.track_range):
            self.zheng_age[i] = iyr - 1972
            self.jane_age[i]  = iyr - 1974
        
    def calculate_pension(self, year_in_future, print_flag = False):
        self.jane_salary_at_retirement = self.jane_salary_today* \
            (1+self.jane_annual_salary_change)**(self.jane_retirement_year-self.current_year)
 
        pension_table = [[34.5, 36.8, 39.1, 41.4, 43.7, 46.0, 48.3, 50.6, 52.9, 55.2, 57.5],
                         [36.0, 38.4, 40.8, 43.2, 45,6, 48.0, 50.4, 52.8, 55.2, 57.6, 60.0],
                         [37.5, 40.0, 42.5, 45.0, 47.5, 50.0, 52.5, 55.0, 57.5, 60.0, 62.5],
                         [39.0, 41.6, 44.2, 46.8, 49.4, 52.0, 54.8, 57.2, 59.8, 62.4, 65.0]]    

        self.jane_tenure_year = self.jane_retirement_year - 2006 
        idx = self.jane_pension_trigger_age - 55
        idy = self.jane_tenure_year - 23
        self.pension_rate = pension_table[idy][idx]*0.01 
        if year_in_future < self.jane_pension_trigger_year:
            self.jane_pension = 0.0
            if print_flag == True:
                print("{:d} pension is not triggered!!".format(year_in_future))
            print_flag = False
            jane_pension = 0.0
        else:
            jane_pension = self.jane_salary_at_retirement * self.pension_rate
            pension_inflation_adjustment = (jane_pension*0.2)*(1+self.inflation)**(year_in_future-self.jane_pension_trigger_year)
            jane_pension = jane_pension + pension_inflation_adjustment

        if print_flag == True:
            print("Jane pension calculation")
            print("Jane tenure year {:d}".format(self.jane_tenure_year)) 
            print("Jane salary at retirement ${:,.0f}".format(self.jane_salary_at_retirement))   
            print("Jane salary at retirement ${:,.0f} per month".format(self.jane_salary_at_retirement/12))     
            print("Jane age at retirement {:d}".format(self.jane_pension_trigger_age)) 
            print("Jane tenure at retirement {:d} years".format(self.jane_tenure_year)) 
            print("pension rate {:,.1%}".format(self.pension_rate))
            print("pension income ${:,.0f} per month".format(jane_pension/12))  
            print("pension income ${:,.0f} per month in today $".format(jane_pension*self.to_dollar_today(self.jane_pension_trigger_year)/12))
            print("--------------------------------------------------------------")

        return jane_pension

    def calculate_ssi(self, year_in_future, print_flag = False):
        self.full_retirement_age = 67
        ss_benefit = {62: 2402.0,
                      63: 2598.0,
                      64: 2813.0,
                      65: 3087.0,
                      66: 3340.0,
                      67: 3594.0,
                      68: 3802.0,
                      69: 4107.0,
                      70: 4507.0}
        self.full_retirement_ssi = ss_benefit[self.full_retirement_age]       

        if year_in_future < self.zheng_ss_trigger_year:
            zheng_ss_income = 0.0
            if print_flag == True:
                print("{:d} social security is not triggered!!".format(year_in_future))

        else:
            ss_income_inflation_adjustment = (1+self.inflation)**(year_in_future-self.zheng_ss_trigger_year)
            zheng_ss_income = ss_benefit[int(self.zheng_ss_trigger_age)]*ss_income_inflation_adjustment

        if print_flag == True:
            print("Zheng social security income calculation")
            print("full retirement age {:d}".format(self.full_retirement_age))        
            print("full retirement year {:d}".format(self.full_retirement_age + 1972))    
            print("full retirement social security income ${:,.0f} per month".format(self.full_retirement_ssi))  
            print("Zheng age at retirement {:d}".format(self.zheng_retirement_age))
            print("Zheng ss trigger age {:d}".format(self.zheng_ss_trigger_age))
            print("Zheng social security income ${:,.0f}".format(zheng_ss_income*12))
            print("Zheng social security income ${:,.0f} per month".format(zheng_ss_income))
            print("--------------------------------------------------------------")

        return zheng_ss_income*12

    def calculate_401k(self, year_in_future, withdraw_method, withdraw_rate=None, print_flag = 'print'): 
        
        if withdraw_method.casefold() == 'lasting' or withdraw_method.casefold() == 'last':
            self.zheng_401k_withdraw_rate = self.standard_investment_return - self.inflation
        else:
            self.zheng_401k_withdraw_rate = withdraw_rate
            
        print("Zheng 401k calculation")
        print("zheng_401k_withdraw_rate   = {:,.2%}".format(self.zheng_401k_withdraw_rate))
        zheng_401k_balance_today = 750*self.KUSD

        # calculate 401k at retirement
        for i, iyr in enumerate(self.track_range):
            # 401k contribution limit
            if iyr > self.zheng_retirement_year:
                current_year_401k_contribution = 0.0

            else:
                current_year_401k_contribution = 20*self.KUSD*(1+self.annual_401k_contribution_limit_increase)**(iyr-2024)
                if print_flag == True:
                    print("{:d} 401k contribution {:,.0f}".format(iyr,current_year_401k_contribution))

            self.zheng_401k_chipin[i] = current_year_401k_contribution
                
            if i==0:
                self.zheng_401k_balance[i] = zheng_401k_balance_today + current_year_401k_contribution
            else:
                self.zheng_401k_balance[i] = self.zheng_401k_balance[i-1] + current_year_401k_contribution
                capital_gain = self.zheng_401k_balance[i] * self.standard_investment_return
                # print("Zheng 401k capital gain ${:,.0f}".format(capital_gain))
                self.zheng_401k_balance[i] = self.zheng_401k_balance[i] + capital_gain
            
            if iyr >= self.zheng_401k_trigger_year:
                self.zheng_401k_withdraw[i] = self.zheng_401k_balance[i]*self.zheng_401k_withdraw_rate
                self.zheng_401k_balance[i] = self.zheng_401k_balance[i] - self.zheng_401k_withdraw[i] 
                # print("Zheng 401k withdraw ${:,.0f}".format(withdraw_401k))
            self.zheng_401k_IAB[i] = self.zheng_401k_balance[i]*self.to_dollar_today(iyr)

            if print_flag.casefold() == 'print':
                print("{:d} 401k balance ${:,.0f}, inflation adjusted: ${:,.0f}".format(iyr,self.zheng_401k_balance[i], self.zheng_401k_IAB[i]))
            
        if print_flag.casefold() == 'figure':
            plt.figure()
            plt.plot(self.track_range, self.zheng_401k_balance/self.KUSD, 'b-', label='Nominal')
            plt.plot(self.track_range, self.zheng_401k_IAB/self.KUSD, 'r--', label='Inflation Adjusted')
            plt.grid(True)
            plt.xlabel('Year')
            plt.ylabel('401k Balance (k$)')
            plt.title('401k Balance Over Time')
            plt.legend()
            plt.show()
            # print(zheng_401k_balance[i])
            # print(track_range[i])
          
    def calculate_403b(self, year_in_future, withdraw_method, print_flag = False): 
        print("Jane 403b calculation")
        jane_403b_balance_today = 250*self.KUSD
        
        # calculate 403b at retirement
        if withdraw_method.casefold() == 'lasting' or withdraw_method.casefold() == 'last':
            self.jane_403b_withdraw_rate = (1.0 + self. standard_investment_return) / (1.0 + self.inflation) - 1.0
        print("jane_403b_withdraw_rate    = {:,.2%}".format(self.jane_403b_withdraw_rate))
        
        for i, iyr in enumerate(self.track_range):
            # 403b contribution

            if iyr > self.jane_retirement_year:
                current_year_403b_contribution = 0.0
            else:
                current_year_403b_contribution = 0.25*self.jane_salary_today*(1+self.jane_annual_salary_change)**(iyr-self.current_year)
                if print_flag == True:
                    print("{:d} 403b contribution {:,.0f}".format(iyr,current_year_403b_contribution))
                    
            self.jane_403b_chipin[i] = current_year_403b_contribution
                
            if i==0:
                self.jane_403b_balance[i] = jane_403b_balance_today + current_year_403b_contribution
            else:
                self.jane_403b_balance[i] = self.jane_403b_balance[i-1] + current_year_403b_contribution
                capital_gain = self.jane_403b_balance[i] * self.standard_investment_return
                # print("Jane 403b capital gain ${:,.0f}".format(capital_gain))
                self.jane_403b_balance[i] = self.jane_403b_balance[i] + capital_gain
            
            if iyr >= self.jane_403b_trigger_year:
                self.jane_403b_withdraw[i] = self.jane_403b_balance[i]*self.jane_403b_withdraw_rate
                self.jane_403b_balance[i] = self.jane_403b_balance[i] - self.jane_403b_withdraw[i]
                # print("Jane 403b withdraw ${:,.0f}".format(withdraw_403b))
            self.jane_403b_IAB[i] = self.jane_403b_balance[i]*self.to_dollar_today(iyr)
            if print_flag == True:                
                print("{:d} 403b balance ${:,.0f}, inflation adjusted: ${:,.0f}".format(iyr,self.jane_403b_balance[i], self.jane_403b_IAB[i]))

        
    def calculate_retirement_expense(self, fixed_budget = None, fixed = True, print_flag = True):
        if fixed == True:
            self.annual_spend_limit = fixed_budget
        else:
            property_tax = 15000
            property_insurance = 3000
            property_maintenance = 5000
            property_utilities = 600*6 + 200*6
            food_expense = 2000*12
            travel_expense = 36000
            lodging_expense = 1200*6
            miscellaneous_expense = 1000*12
            self.annual_spend_limit = property_tax + property_insurance + property_maintenance + property_utilities +\
                                      food_expense + travel_expense + lodging_expense + miscellaneous_expense
        for i, iyr in enumerate(self.track_range):
            self.expense[i] = self.to_dollar_future(iyr)*self.annual_spend_limit
            if print_flag == True:
                print("{:d} expense ${:,.0f}".format(iyr,self.expense[i]))
            
    def calculate_salary_income(self):
        for i, iyr in enumerate(self.track_range):
            if iyr <= self.zheng_retirement_year:
                self.zheng_job_income[i] = self.zheng_salary_today*(1+self.zheng_annual_salary_change)**(iyr-self.current_year)
            if iyr <= self.jane_retirement_year:
                self.jane_job_income[i]  = self.jane_salary_today*(1+self.jane_annual_salary_change)**(iyr-self.current_year)

    def est_income_tax(self, income, year, print_flag = False):
        
        bracket  = [22000, 89450, 190750, 364200, 462500, 693750]
        tax_rate = [0.10,  0.12,  0.22,   0.24,   0.32,   0.35]
        tax_zone = np.linspace(0,0,len(bracket))
        tax_stack = np.linspace(0,0,len(bracket))
        
        adjustment = (1+self.inflation)**(year-self.current_year)
        for i,ix in enumerate(bracket):
            if i<1:
                tax_zone[i] = adjustment*bracket[i]*tax_rate[i]
                tax_stack[i] = tax_zone[i]
            else:
                tax_zone[i] = adjustment*(bracket[i]-bracket[i-1])*tax_rate[i]
                tax_stack[i] = tax_zone[i] + tax_zone[i-1]
        
        fed_tax = 0.0
        for i,ix in enumerate(bracket):
            if income>=bracket[i]:
                fed_tax = tax_stack[i] + (income-bracket[i])*tax_rate[i]

        ss_income = self.calculate_ssi(year)
        pension_income = self.calculate_pension(year)
        taxable_state = income - ss_income - pension_income
        state_tax = taxable_state*self.state_tax_rate 
        
        tax = fed_tax + state_tax
        
        if print_flag == True:
            print('fed_tax =', fed_tax)      
            print('state_tax =', state_tax)            

        return tax         


    def export_to_spreadsheet(self):
        # Create a dictionary of all time series data
        data = {
            'Year': self.track_range,
            'Zheng Age': self.zheng_age,
            'Jane Age': self.jane_age,
            'Zheng 401k Balance': self.zheng_401k_balance,
            'Zheng 401k Contributions': self.zheng_401k_chipin,
            'Zheng 401k Withdrawals': self.zheng_401k_withdraw,
            'Jane 403b Balance': self.jane_403b_balance,
            'Jane 403b Contributions': self.jane_403b_chipin,
            'Jane 403b Withdrawals': self.jane_403b_withdraw,
            'Zheng Salary Income': self.zheng_job_income,
            'Jane Salary Income': self.jane_job_income,
            'Social Security Income': self.ss_income,
            'Pension Income': self.pension_income,
            'Annual Expenses': self.expense,
            'Gross Income': self.gross_income,
            'IA Income': self.income_IAB,
            'After-Tax Income': self.income_after_tax,
            'Cash Position': self.cash_position
        }
        
        # Create DataFrame and export to Excel
        df = pd.DataFrame(data)
        df.to_excel('retirement_projections.xlsx', index=False)

    def calculate_cash_flow(self, print_flag):
        self.cash_position[0] = self.cash_today 
        for i, iyr in enumerate(self.track_range):
            self.pension_income[i] = self.calculate_pension(iyr)
            self.ss_income[i]      = self.calculate_ssi(iyr)
            self.gross_income[i]   = self.zheng_job_income[i] + self.zheng_401k_withdraw[i] + self.ss_income[i] + \
                                     self.jane_job_income[i]  + self.jane_403b_withdraw[i]  + self.pension_income[i] 
            self.income_IAB[i]        = self.gross_income[i] * self.to_dollar_today(iyr)
            self.income_after_tax[i]  = self.gross_income[i] - self.est_income_tax(self.gross_income[i], iyr)                         
            if i<1:
                self.cash_position[0] = self.cash_today - self.expense[i]
            else:
                self.cash_position[i] = self.cash_position[i-1] - self.expense[i] + self.income_after_tax[i]
                
            if print_flag == True:                
                print("{:d} income ${:,.0f}, inflation adjusted: ${:,.0f}".format(iyr,self.gross_income[i], self.gross_income[i]*self.to_dollar_today(iyr)))
    
    def calculate_expense(self):
        df = pd.read_csv('expense.csv')

        # Fill in yearly/monthly values where one is missing
        for index, row in df.iterrows():
            # Pre-retirement calculations
            if pd.isna(row['Pre-retire-yearly']) and pd.notna(row['Pre-retire-monthly']):
                df.at[index, 'Pre-retire-yearly'] = row['Pre-retire-monthly'] * 12
            elif pd.isna(row['Pre-retire-monthly']) and pd.notna(row['Pre-retire-yearly']):
                df.at[index, 'Pre-retire-monthly'] = row['Pre-retire-yearly'] / 12

            # Post-retirement calculations  
            if pd.isna(row['Post-retire-yearly']) and pd.notna(row['Post-retire-monthly']):
                df.at[index, 'Post-retire-yearly'] = row['Post-retire-monthly'] * 12
            elif pd.isna(row['Post-retire-monthly']) and pd.notna(row['Post-retire-yearly']):
                df.at[index, 'Post-retire-monthly'] = row['Post-retire-yearly'] / 12

        self.pre_retire_expense = df['Pre-retire-yearly'].sum()
        self.post_retire_expense = df['Post-retire-yearly'].sum()
        # Calculate small property expense (70% for property, 100% for other categories)
        property_mask = df['Category'] == 'Property'
        property_expenses = df[property_mask]['Post-retire-yearly'].sum() * 0.70
        other_expenses = df[~property_mask]['Post-retire-yearly'].sum()
        self.small_property_expense = property_expenses + other_expenses

        # Sort DataFrame by Post-retire-yearly in descending order
        df = df.sort_values(by='Post-retire-yearly', ascending=False)

        print(df)
        print("pre_retire_expense = ${:,.0f}".format(self.pre_retire_expense))
        print("post_retire_expense = ${:,.0f}".format(self.post_retire_expense))
        print("small_property_expense = ${:,.0f}".format(self.small_property_expense))
        return df