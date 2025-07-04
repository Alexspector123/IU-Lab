package com.example.demo.services.impl;

import com.example.demo.dto.*;

import com.example.demo.entity.User;
import com.example.demo.repository.UserRepository;
import com.example.demo.services.EmailService;
import com.example.demo.services.UserService;
import com.example.demo.utils.AccountUtilis;

import java.math.BigDecimal;
import java.math.BigInteger;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class UserServiceImpl implements UserService {

    @Autowired
    UserRepository userRepository;
    EmailService emailService;

    @Override
    public BankResponse createAccount(UserRequest userRequest) {
        // Check whether email exsit in database
        if (userRepository.existsByEmail(userRequest.getEmail())) {
            // if exsit return BankResponse with response
            return BankResponse.builder()
                    .responseCode(AccountUtilis.ACCOUNT_EXISTS_CODE)
                    .responseMessage(AccountUtilis.ACCOUNT_EXISTS_MESSAGE)
                    .AccountInfo(null)
                    .build();
        }
        // Using builder to create new User you call use contructor instead
        // User newUser = new User("Nghia", "Nguyen", "Trung", "123 Linh Trung"...)
        User newUser = User.builder()
                .firstName(userRequest.getFirstName())
                .lastName(userRequest.getLastName())
                .otherName(userRequest.getOtherName())
                .address(userRequest.getAddress())
                .sateOfOrigin(userRequest.getSateOfOrigin())
                .accountNumber(AccountUtilis.generateAccountNumber())
                .accountBalance(BigDecimal.ZERO)
                .phoneNumber(userRequest.getPhoneNumber())
                .alternativePhoneNumber(userRequest.getAlternativePhoneNumber())
                .email(userRequest.getEmail())
                .status("ACTIVE")
                .build();
        // Save user to database by repository
        User savedUser = userRepository.save(newUser);
        // Create account Info
        AccountInfo accountInfo = AccountInfo.builder()
                .accountBalance(savedUser.getAccountBalance())
                .accountNumber(savedUser.getAccountNumber())
                .accountName(savedUser.getFirstName() + " "
                        + savedUser.getLastName() + " "
                        + savedUser.getOtherName())
                .build();
        return BankResponse.builder()
                .responseCode(AccountUtilis.ACCOUNT_CREATION_SUCCESS_CODE)
                .responseMessage(AccountUtilis.ACCOUNT_CREATION_SUCCESS_MASSAGE)
                .AccountInfo(accountInfo)
                .build();
    }

    @Override
    public List<UserDTO> getAllUsers() {
        List<User> users = userRepository.findAll();
        return users.stream()
                .map(user -> new UserDTO(
                        user.getId(),
                        user.getFirstName(),
                        user.getLastName(),
                        user.getOtherName(),
                        user.getGender(),
                        user.getAddress(),
                        user.getSateOfOrigin(),
                        user.getAccountNumber(),
                        user.getAccountBalance(),
                        user.getPhoneNumber(),
                        user.getAlternativePhoneNumber(),
                        user.getEmail(),
                        user.getStatus(),
                        user.getCreateAt(),
                        user.getModifiedAt()))
                .collect(Collectors.toList());

    }

    @Override
    public UserDTO getUserById(Long id) {
        User user = userRepository.findById(id).orElse(null);
        if (user != null) {
                return new UserDTO(
                        user.getId(),
                        user.getFirstName(),
                        user.getLastName(),
                        user.getOtherName(),
                        user.getGender(),
                        user.getAddress(),
                        user.getSateOfOrigin(),
                        user.getAccountNumber(),
                        user.getAccountBalance(),
                        user.getPhoneNumber(),
                        user.getAlternativePhoneNumber(),
                        user.getEmail(),
                        user.getStatus(),
                        user.getCreateAt(),
                        user.getModifiedAt());
        } else {
                return null;
        }
    }

    @Override
    public UserDTO updateUser(Long id, UserRequest request) {
        User user = userRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("User not found with ID: " + id));

        user.setFirstName(request.getFirstName());
        user.setLastName(request.getLastName());
        user.setOtherName(request.getOtherName());
        user.setGender(request.getGender());
        user.setAddress(request.getAddress());
        user.setSateOfOrigin(request.getSateOfOrigin());
        user.setPhoneNumber(request.getPhoneNumber());
        user.setAlternativePhoneNumber(request.getAlternativePhoneNumber());
        user.setEmail(request.getEmail());

        User updatedUser = userRepository.save(user);

        return new UserDTO(
                updatedUser.getId(),
                updatedUser.getFirstName(),
                updatedUser.getLastName(),
                updatedUser.getOtherName(),
                updatedUser.getGender(),
                updatedUser.getAddress(),
                updatedUser.getSateOfOrigin(),
                updatedUser.getAccountNumber(),
                updatedUser.getAccountBalance(),
                updatedUser.getPhoneNumber(),
                updatedUser.getAlternativePhoneNumber(),
                updatedUser.getEmail(),
                updatedUser.getStatus(),
                updatedUser.getCreateAt(),
                updatedUser.getModifiedAt());
    }

    @Override
    public void deleteUser(Long id) {
        if (!userRepository.existsById(id)) {
            throw new RuntimeException("User not found with ID: " + id);
        }
        userRepository.deleteById(id);
    }
    
}
