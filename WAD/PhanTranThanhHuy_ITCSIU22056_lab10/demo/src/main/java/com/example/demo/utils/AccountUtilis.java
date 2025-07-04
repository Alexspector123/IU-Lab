package com.example.demo.utils;

import java.time.Year;

public class AccountUtilis {
    public static final String ACCOUNT_EXISTS_CODE = "001";
    public static final String ACCOUNT_EXISTS_MESSAGE = "Account has been successfully created";
    public static final String ACCOUNT_CREATION_SUCCESS_CODE = "002";
    public static final String ACCOUNT_CREATION_SUCCESS_MASSAGE = "This user already exists!";

    public static String generateAccountNumber() {
        // 2023 + randonSixDigits
        Year currentYear = Year.now();
        int min = 100000;
        int max = 999999;
        int randNumber = (int) Math.floor(Math.random() * (max - min + 1));
        String year = String.valueOf(currentYear);
        String randomNumber = String.valueOf(randNumber);
        StringBuilder accountNumber = new StringBuilder();
        return accountNumber
                .append(year)
                .append(randomNumber)
                .toString();
    }
}