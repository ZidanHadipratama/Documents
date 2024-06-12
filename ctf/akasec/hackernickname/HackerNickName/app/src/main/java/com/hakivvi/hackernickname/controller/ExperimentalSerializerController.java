package com.hakivvi.hackernickname.controller;

import jakarta.servlet.http.HttpServletRequest;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import com.hakivvi.hackernickname.util.ExperimentalSerializer;
import java.util.HashMap;

@Controller
@RequestMapping("/ExperimentalSerializer")
public class ExperimentalSerializerController {

    @GetMapping
    public String experimentalSerializer(@RequestParam(value = "serialized", required = false) String serialized, HttpServletRequest request, Model model) {
        if (!request.getRemoteAddr().equals("127.0.0.1"))
            return "redirect:/";
        if (serialized != null)
        {
            HashMap<String, Object> result = ExperimentalSerializer.deserialize(serialized);
            model.addAttribute("result", result.toString());
        }
        return "serializer";
    }
}
