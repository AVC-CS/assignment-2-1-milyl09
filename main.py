def main():
    
    ##################################################
    #Comlete your code here
    #Use m_perc and f_perc for your results
    ##################################################
    
    total_male = int(input("What is the number of males in class?: "))
    total_female = int(input("What is your percentage of Females in class?: "))

    
    Total_num = total_male + total_female 
    m_perc = total_male/Total_num * 100
    f_perc = total_female/Total_num * 100
    
    print (Total_num)
    print (m_perc)
    print (f_perc)
    
    print(f'percentage of females: \t {f_perc:.2f}') 
    print(f'percentage of males: \t {m_perc:.2f}')
    ########################################
    # Do not delete the return statement
    ########################################
    
    return m_perc, f_perc


if __name__ == '__main__':
    main()
