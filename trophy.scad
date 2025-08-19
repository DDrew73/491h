// OpenSCAD Code for 3D Printable Trophy

// Base Pedestal
module pedestal() {
    cube([100, 100, 25]); // 4x4 inches (100mm x 100mm) and 1 inch (25mm) height
    translate([50, 0, 12.5]) // Positioning text on the front face of the base
    rotate([90, 0, 0]) // Rotate text to align with the front face
    linear_extrude(2.5)
    text("491H Fall 2024", size = 10, valign = "center", halign = "center");
}

// Romi Chassis Shape
module romi_chassis() {
    // Main body of the chassis
    translate([50, 50, 60]) // Correctly position above the base center
    cylinder(h = 20, r = 50, center = true); // Approximate the round shape of the chassis

    // Wheels
    translate([50, 80, 35])
    rotate([90, 0, 0])
    cylinder(h = 10, r = 20, center = true); // Right wheel
    translate([50, 20, 35])
    rotate([90, 0, 0])
    cylinder(h = 10, r = 20, center = true); // Left wheel

    // Front caster
    translate([50, 10, 25])
    sphere(r = 10); // Approximate the front caster as a sphere
}

// Infinity Symbol for Infinity Cup
module infinity_symbol() {
    translate([50, 50, 65]) // Position on top of the chassis
    scale([1, 0.5, 1])
    rotate([90, 0, 0])
    torus(10, 5); // Create an infinity symbol using two torus shapes
}

// Clock Symbol for Time Trial
module clock_symbol() {
    translate([50, 50, 65]) // Position on top of the chassis
    cylinder(h = 5, r = 20, center = true); // Clock face
    translate([50, 50, 67])
    rotate([0, 0, 45])
    cube([2, 10, 2], center = true); // Clock hand
    translate([50, 50, 67])
    rotate([0, 0, -45])
    cube([2, 15, 2], center = true); // Clock hand
}

// Main Trophy Assembly
module trophy(version) {
    pedestal();
    romi_chassis();
    if (version == "Infinity Cup") {
        infinity_symbol();
    } else if (version == "Time Trial") {
        clock_symbol();
    }
}

// Render the Infinity Cup Trophy
trophy("Infinity Cup");
