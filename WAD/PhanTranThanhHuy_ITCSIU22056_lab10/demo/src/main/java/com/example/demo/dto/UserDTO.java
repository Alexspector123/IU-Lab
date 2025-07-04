package com.example.demo.dto;

import java.math.BigDecimal;
import java.time.LocalDateTime;

import lombok.Builder;

    @Builder
public class UserDTO {
    private Long id;
    private String first_name;
    private String last_name;
    private String other_Name;
    private String gender;
    private String address;
    private String sate_of_origin;
    private String account_number;
    private BigDecimal account_balance;
    private String email;
    private String phone_number;
    private String alternative_phone_number;
    private String status;
    private LocalDateTime create_at;
    private LocalDateTime modified_at;


    public UserDTO(Long id, String first_name, String last_name, String other_Name, String gender, String address,
                   String sate_of_origin, String account_number, BigDecimal account_balance, String email,
                   String phone_number, String alternative_phone_number, String status, LocalDateTime create_at,
                   LocalDateTime modified_at) {
        this.id = id;
        this.first_name = first_name;
        this.last_name = last_name;
        this.other_Name = other_Name;
        this.gender = gender;
        this.address = address;
        this.sate_of_origin = sate_of_origin;
        this.account_number = account_number;
        this.account_balance = account_balance;
        this.email = email;
        this.phone_number = phone_number;
        this.alternative_phone_number = alternative_phone_number;
        this.status = status;
        this.create_at = create_at;
        this.modified_at = modified_at;
    }

    // Getters and setters
    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }

    public String getFirstName() {
        return first_name;
    }
    public void setFirstName(String first_name) {
        this.first_name = first_name;
    }

    public String getLastName() {
        return last_name;
    }
    public void setLastName(String last_name) {
        this.last_name = last_name;
    }

    public String getOtherName() {
        return other_Name;
    }
    public void setOtherName(String other_Name) {
        this.other_Name = other_Name;
    }

    public String getGender() {
        return gender;
    }
    public void setGender(String gender) {
        this.gender = gender;
    }

    public String getAddress() {
        return address;
    }
    public void setAddress(String address) {
        this.address = address;
    }

    public String getSateOfOrigin() {
        return sate_of_origin;
    }
    public void setSateOfOrigin(String sate_of_origin) {
        this.sate_of_origin = sate_of_origin;
    }

    public String getAccountNumber() {
        return account_number;
    }
    public void setAccountNumber(String account_number) {
        this.account_number = account_number;
    }

    public BigDecimal getAccountBalance() {
        return account_balance;
    }
    public void setAccountBalance(BigDecimal account_balance) {
        this.account_balance = account_balance;
    }

    public String getEmail() {
        return email;
    }
    public void setEmail(String email) {
        this.email = email;
    }

    public String getPhoneNumber() {
        return phone_number;
    }
    public void setPhoneNumber(String phone_number) {
        this.phone_number = phone_number;
    }

    public String getAlternativePhoneNumber() {
        return alternative_phone_number;
    }
    public void setAlternativePhoneNumber(String alternative_phone_number) {
        this.alternative_phone_number = alternative_phone_number;
    }

    public String getStatus() {
        return status;
    }
    public void setStatus(String status) {
        this.status = status;
    }

    public LocalDateTime getCreateAt() {
        return create_at;
    }
    public void setCreateAt(LocalDateTime create_at) {
        this.create_at = create_at;
    }

    public LocalDateTime getModifiedAt() {
        return modified_at;
    }
    public void setModifiedAt(LocalDateTime modified_at) {
        this.modified_at = modified_at;
    }
}
