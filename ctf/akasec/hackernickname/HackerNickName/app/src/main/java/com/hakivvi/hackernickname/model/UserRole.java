package com.hakivvi.hackernickname.model;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

public class UserRole {
    public boolean admin;

    @JsonCreator
    public UserRole(@JsonProperty("admin") boolean admin) {
        this.admin = admin;
    }
}
