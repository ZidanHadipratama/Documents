package com.hakivvi.hackernickname.model;

import com.fasterxml.jackson.annotation.JsonProperty;

public class SerializationItem {
    @JsonProperty(required = true)
    public String type;
    @JsonProperty(required = true)
    public String name;
    @JsonProperty(required = true)
    public String value;
}
