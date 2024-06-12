package com.hakivvi.hackernickname.config;

import com.fasterxml.jackson.databind.InjectableValues;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import com.hakivvi.hackernickname.model.UserRole;

@Configuration
public class JacksonConfig {
    @Bean
    public ObjectMapper objectMapper() {
        ObjectMapper objectMapper = new ObjectMapper();
        InjectableValues injectableValues = new InjectableValues.Std().addValue(UserRole.class, new UserRole(false));
        objectMapper.setInjectableValues(injectableValues);
        return objectMapper;
    }
}
