package com.f1predictor.ui.dto;

public class ChampionPredictionDto {
    private Integer driver_id;
    private String name;
    private String code;
    private Double predicted_score;

    public Integer getDriver_id() { return driver_id; }
    public void setDriver_id(Integer driver_id) { this.driver_id = driver_id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getCode() { return code; }
    public void setCode(String code) { this.code = code; }

    public Double getPredicted_score() { return predicted_score; }
    public void setPredicted_score(Double predicted_score) { this.predicted_score = predicted_score; }
}
