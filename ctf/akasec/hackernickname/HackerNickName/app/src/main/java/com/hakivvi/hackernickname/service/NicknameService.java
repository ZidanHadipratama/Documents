package com.hakivvi.hackernickname.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;
import org.springframework.util.ResourceUtils;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Random;
import java.util.concurrent.TimeUnit;

@Component
public class NicknameService {
    public final Path filePath;
    private String[] nicknames;
    private final Random random = new Random();

    public NicknameService(@Value("${nicknames.file.path}") String filePath) throws IOException {
        this.filePath = ResourceUtils.getFile(filePath).toPath();
        List<String> lines = Files.readAllLines(this.filePath);
        this.nicknames = lines.toArray(new String[0]);
    }

    public String getNickName() {
        return nicknames[random.nextInt(nicknames.length)];
    }

    public void reload() throws IOException {
        List<String> lines = Files.readAllLines(filePath);
        if (lines.size() > 1 && lines.size() <= 200 && lines.stream().allMatch(nickname -> nickname.matches("[a-zA-Z0-9]{5,50}$"))) {
            this.nicknames = lines.toArray(new String[0]);
        }
    }

    @EnableScheduling
    public static class NickNamesDBUpdate {
        private final NicknameService nicknameService;

        public NickNamesDBUpdate(@Autowired NicknameService nicknameService) {
            this.nicknameService = nicknameService;
        }

        @Scheduled(fixedDelay = 2, timeUnit = TimeUnit.MINUTES)
        public void run() throws IOException, NullPointerException, InterruptedException {
            String filePath = nicknameService.filePath.toString();
            ProcessBuilder pb = new ProcessBuilder("curl", "-f", "http://nicknameservice:5000/getnicknames", "-o", filePath);
            pb.start().waitFor();
            nicknameService.reload();
        }
    }
}