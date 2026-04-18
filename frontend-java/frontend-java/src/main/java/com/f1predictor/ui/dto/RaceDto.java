package com.f1predictor.ui.dto;

public class RaceDto {
    private Integer race_id;
    private Integer season_year;
    private Integer round;
    private Integer circuit_id;
    private String race_name;
    private String date;
    private Integer is_completed;

    public Integer getRace_id() { return race_id; }
    public void setRace_id(Integer race_id) { this.race_id = race_id; }

    public Integer getSeason_year() { return season_year; }
    public void setSeason_year(Integer season_year) { this.season_year = season_year; }

    public Integer getRound() { return round; }
    public void setRound(Integer round) { this.round = round; }

    public Integer getCircuit_id() { return circuit_id; }
    public void setCircuit_id(Integer circuit_id) { this.circuit_id = circuit_id; }

    public String getRace_name() { return race_name; }
    public void setRace_name(String race_name) { this.race_name = race_name; }

    public String getDate() { return date; }
    public void setDate(String date) { this.date = date; }

    public Integer getIs_completed() { return is_completed; }
    public void setIs_completed(Integer is_completed) { this.is_completed = is_completed; }
}
