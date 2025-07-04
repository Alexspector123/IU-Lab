package com.example.demo.services;

import com.example.demo.dto.BankResponse;
import com.example.demo.dto.UserRequest;
import com.example.demo.dto.UserDTO;

import java.util.List;

public interface UserService {
    public BankResponse createAccount(UserRequest userRequest);
    public List<UserDTO> getAllUsers();
    public UserDTO getUserById(Long id);
    public UserDTO updateUser(Long id, UserRequest request);
    public void deleteUser(Long id);
}
