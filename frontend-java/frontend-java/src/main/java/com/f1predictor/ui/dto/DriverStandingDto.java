package com.f1predictor.ui.dto;

public class DriverStandingDto {
    private Integer position;
    private Integer driver_id;
    private String driver_name;
    private String code;
    private Double points;

    public Integer getPosition() { return position; }
    public void setPosition(Integer position) { this.position = position; }

    public Integer getDriver_id() { return driver_id; }
    public void setDriver_id(Integer driver_id) { this.driver_id = driver_id; }

    public String getDriver_name() { return driver_name; }
    public void setDriver_name(String driver_name) { this.driver_name = driver_name; }

    public String getCode() { return code; }
    public void setCode(String code) { this.code = code; }

    public Double getPoints() { return points; }
    public void setPoints(Double points) { this.points = points; }
}
