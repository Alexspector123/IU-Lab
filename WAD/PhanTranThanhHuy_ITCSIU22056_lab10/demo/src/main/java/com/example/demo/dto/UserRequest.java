package com.example.demo.dto;

import lombok.*;

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class UserRequest {
    private String firstName;
    private String lastName;
    private String otherName;
    private String gender;
    private String address;
    private String sateOfOrigin;
    private String accountNumber;
    private String email;
    private String phoneNumber;
    private String alternativePhoneNumber;
    private String status;
}