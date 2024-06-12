package com.hakivvi.hackernickname.model;

import com.fasterxml.jackson.annotation.JacksonInject;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotEmpty;

import java.util.HashMap;
import java.util.Map;

public class Hacker {
    @NotBlank
    private final String firstName;
    @NotBlank
    private final String lastName;
    @NotBlank
    private final String favouriteCategory;
    private final UserRole role;
    private String nickName;

    @JsonCreator
    public Hacker(@JsonProperty(value = "firstName", required = true) String firstName,
                  @JsonProperty(value = "lastName", required = true) String lastName,
                  @JsonProperty(value = "favouriteCategory", required = true) String favouriteCategory,
                  @JacksonInject UserRole hackerRole) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.favouriteCategory = favouriteCategory;
        this.role = hackerRole;
    }

    public Boolean isAdmin() {
        return (role.admin);
    }

    public void setNickName(String nickName) {
        this.nickName = nickName;
    }

    public Map<String, Object> getInfo() {
        Map<String, Object> hackerInfo = new HashMap<>();
        hackerInfo.put("nickname", nickName);
        hackerInfo.put("admin", isAdmin());
        return hackerInfo;
    }
}
