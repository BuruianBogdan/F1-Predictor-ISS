package com.f1predictor.ui.controller;

import com.f1predictor.ui.dto.*;
import com.f1predictor.ui.service.FlaskApiService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
public class WebController {

    private final FlaskApiService flaskApiService;

    public WebController(FlaskApiService flaskApiService) {
        this.flaskApiService = flaskApiService;
    }

    @GetMapping("/")
    public String index(Model model) {
        model.addAttribute("pageTitle", "Dashboard");
        model.addAttribute("driverCount", flaskApiService.getDrivers().size());
        model.addAttribute("constructorCount", flaskApiService.getConstructors().size());
        model.addAttribute("circuitCount", flaskApiService.getCircuits().size());
        model.addAttribute("raceCount", flaskApiService.getRaces().size());
        return "index";
    }

    @GetMapping("/drivers")
    public String drivers(Model model) {
        model.addAttribute("pageTitle", "Drivers");
        model.addAttribute("drivers", flaskApiService.getDrivers());
        return "drivers";
    }

    @GetMapping("/constructors")
    public String constructors(Model model) {
        model.addAttribute("pageTitle", "Constructors");
        model.addAttribute("constructors", flaskApiService.getConstructors());
        return "constructors";
    }

    @GetMapping("/circuits")
    public String circuits(Model model) {
        model.addAttribute("pageTitle", "Circuits");
        model.addAttribute("circuits", flaskApiService.getCircuits());
        return "circuits";
    }

    @GetMapping("/races")
    public String races(Model model) {
        model.addAttribute("pageTitle", "Races");
        model.addAttribute("races", flaskApiService.getRaces());
        return "races";
    }

    @GetMapping("/results")
    public String results(Model model) {
        model.addAttribute("pageTitle", "Results");
        model.addAttribute("results", flaskApiService.getResults());
        return "results";
    }

    @GetMapping("/standings")
    public String standings(Model model) {
        model.addAttribute("pageTitle", "Standings");
        model.addAttribute("driverStandings", flaskApiService.getDriverStandings());
        model.addAttribute("constructorStandings", flaskApiService.getConstructorStandings());
        return "standings";
    }

    @GetMapping("/predictions")
    public String predictions(@RequestParam(value = "raceId", required = false) Integer raceId,
                              Model model) {
        model.addAttribute("pageTitle", "Predictions");
        model.addAttribute("championPredictions", flaskApiService.getChampionPrediction());

        if (raceId != null) {
            model.addAttribute("selectedRaceId", raceId);
            model.addAttribute("racePredictions", flaskApiService.getRacePrediction(raceId));
        }

        model.addAttribute("races", flaskApiService.getRaces());
        return "predictions";
    }

    @GetMapping("/import")
    public String importPage(Model model) {
        model.addAttribute("pageTitle", "Import Historical Data");
        return "import";
    }

    @PostMapping("/import")
    public String importData(@RequestParam("startYear") Integer startYear,
                             @RequestParam("endYear") Integer endYear,
                             Model model) {
        ImportResponseDto response = flaskApiService.importHistoricalData(startYear, endYear);
        model.addAttribute("pageTitle", "Import Historical Data");
        model.addAttribute("importResponse", response);
        return "import";
    }
}