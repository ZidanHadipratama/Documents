package com.hakivvi.hackernickname.controller;

import com.hakivvi.hackernickname.util.JwtUtil;
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.Arrays;
import java.util.Optional;

@Controller
@RequestMapping("/nickname")
public class NickNameController {
    @Autowired
    private JwtUtil jwtUtil;

    @GetMapping(produces = "text/html")
    public String get(Model model, HttpServletRequest request) {
        Cookie[] cookies = request.getCookies();
        if (cookies == null || cookies.length == 0)
            return "redirect:/";
        Optional<Cookie> jwtCookie = Arrays.stream(cookies)
                .filter(cookie -> "jwt".equals(cookie.getName()))
                .findFirst();
        if (jwtCookie.isEmpty() || !jwtUtil.validateToken(jwtCookie.get().getValue()))
            return "redirect:/";
        model.addAttribute("nickname", jwtUtil.extractClaims(jwtCookie.get().getValue()).get("nickname"));
        return "nickname";
    }
}
