package com.hakivvi.hackernickname.controller;

import com.hakivvi.hackernickname.service.NicknameService;
import com.hakivvi.hackernickname.util.JwtUtil;
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.Arrays;
import java.util.Optional;

@Controller
@RequestMapping("/admin")
public class AdminController {
    @Autowired
    private JwtUtil jwtUtil;
    @Autowired
    private NicknameService nicknameService;

    private boolean isAdmin(Cookie[] cookies) {
        if (cookies == null || cookies.length == 0)
            return false;
        String jwtToken;
        Optional<Cookie> jwtCookie = Arrays.stream(cookies)
                .filter(cookie -> "jwt".equals(cookie.getName()))
                .findFirst();
        if (jwtCookie.isPresent()) {
            jwtToken = jwtCookie.get().getValue();
            if (jwtUtil.validateToken(jwtToken)) {
                return ((boolean)jwtUtil.extractClaims(jwtToken).get("admin"));
            }
        }
        return false;
    }

    @GetMapping("/update")
    public String get(HttpServletRequest request) {
        if (!isAdmin(request.getCookies()))
            return "redirect:/";

        return "update";
    }

    @PostMapping("/update")
    public ResponseEntity<String> post(@RequestParam("url") String url, HttpServletRequest request) throws NullPointerException, IOException, InterruptedException {
        if (!isAdmin(request.getCookies()))
            return ResponseEntity.status(401).body("You are not an admin.");
        URL parsedUrl;
        try {
            parsedUrl = new URL(url);
        } catch (MalformedURLException e) {
            return ResponseEntity.status(401).body(e.getMessage());
        }
        if (!parsedUrl.getProtocol().equals("http") || !parsedUrl.getHost().equals("nicknameservice") || parsedUrl.getPort() != 5000)
            return ResponseEntity.status(401).body("Invalid URL");
        ProcessBuilder pb = new ProcessBuilder("curl", "-f", url, "-o", nicknameService.filePath.toString());
        Process p = pb.start();
        p.waitFor();
        //System.out.println(new String(p.getErrorStream().readAllBytes(), StandardCharsets.UTF_8));
        nicknameService.reload();
        return ResponseEntity.ok("updated.");
    }
}
