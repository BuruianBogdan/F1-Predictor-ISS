package com.f1predictor.ui.dto;

import java.util.Map;

public class ImportResponseDto {
    private String message;
    private Map<String, Integer> summary;

    public String getMessage() { return message; }
    public void setMessage(String message) { this.message = message; }

    public Map<String, Integer> getSummary() { return summary; }
    public void setSummary(Map<String, Integer> summary) { this.summary = summary; }
}