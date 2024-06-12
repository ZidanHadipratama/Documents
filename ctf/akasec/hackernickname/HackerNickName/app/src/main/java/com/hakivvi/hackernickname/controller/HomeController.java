package com.hakivvi.hackernickname.controller;

import com.hakivvi.hackernickname.model.Hacker;
import com.hakivvi.hackernickname.service.NicknameService;
import com.hakivvi.hackernickname.util.JwtUtil;
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.Arrays;
import java.util.Map;
import java.util.Optional;

@Controller
@RequestMapping("/")
public class HomeController {
    @Autowired
    private JwtUtil jwtUtil;
    @Autowired
    private NicknameService nicknameService;

    @GetMapping
    public String get(HttpServletRequest request) {
        Cookie[] cookies = request.getCookies();
        if (cookies == null || cookies.length == 0)
            return "home";
        String jwtToken;
        Optional<Cookie> jwtCookie = Arrays.stream(cookies)
                .filter(cookie -> "jwt".equals(cookie.getName()))
                .findFirst();
        if (jwtCookie.isPresent()) {
            jwtToken = jwtCookie.get().getValue();
            if (jwtUtil.validateToken(jwtToken))
                return "redirect:/nickname";
        }
        return "home";
    }

    @PostMapping(consumes="application/json")
    public void post(@RequestBody @Valid Hacker hacker, HttpServletResponse response) {
        hacker.setNickName(nicknameService.getNickName());
        String token = jwtUtil.generateToken(hacker.getInfo());
        Cookie cookie = new Cookie("jwt", token);
        cookie.setHttpOnly(true);
        cookie.setPath("/");
        response.addCookie(cookie);
    }
}
