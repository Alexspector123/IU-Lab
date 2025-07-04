package com.example.demo.dto;

import lombok.*;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class BankResponse {
    private String responseCode;
    private String responseMessage;
    private AccountInfo AccountInfo;
}