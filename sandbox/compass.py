import colorutils
import folium
import folium.features
import geomove


def plot_compass():
    """
    Generate basic compass rose directions from a reference point and plot them.
    """
    # Prepare points
    reference = ((51.9624, 7.6256), "Reference")
    points = [reference]
    points.extend(
        [(geomove.move(reference[0], b, 10), str(b.name)) for b in geomove.Bearing]
    )

    # Create colors for each point
    colors = [colorutils.Color(hsv=(0, 0, 0.7))]
    colors.extend(
        [
            colorutils.Color(hsv=((i / len(points) * 360.0), 0.8, 0.7))
            for i in range(len(points))
        ]
    )

    # Bearing abbreviations
    abbreviations = {
        "Reference": "R",
        geomove.Bearing.NORTH.name: "N",
        geomove.Bearing.NORTH_EAST.name: "NE",
        geomove.Bearing.EAST.name: "E",
        geomove.Bearing.SOUTH_EAST.name: "SE",
        geomove.Bearing.SOUTH.name: "S",
        geomove.Bearing.SOUTH_WEST.name: "SW",
        geomove.Bearing.WEST.name: "W",
        geomove.Bearing.NORTH_WEST.name: "NW",
    }

    # Create map
    m = folium.Map(location=reference[0], zoom_start=12)

    # Plot points
    for p, c in zip(points, colors):
        folium.CircleMarker(
            location=p[0],
            radius=5,
            color=c.hex,
            fill=True,
            fill_color=c.hex,
            fill_opacity=0.5,
            popup=p[1],
        ).add_to(m)

    # Create a map centered on reference point
    m = folium.Map(reference[0], zoom_start=12, tiles="cartodb positron")
    folium.TileLayer("cartodbdark_matter").add_to(m)
    folium.TileLayer("openstreetmap").add_to(m)

    # Plot all points
    for p, point in enumerate(points):
        popup_text = folium.Html(
            "<p>"
            + f"Bearing: {point[1]}</br>"
            + f"Location (lat/lon): {point[0][0]}, {point[0][1]}</br>"
            + "</p>",
            script=True,
        )
        marker = folium.CircleMarker(
            point[0],
            popup=folium.Popup(popup_text, max_width=450, sticky=True),
            color=colors[p].hex,
            radius=8,
            fill=True,
            fillOpacity=1.0,
        )
        marker.options["fillOpacity"] = 1.0
        marker.add_to(m)
        text = folium.Marker(
            point[0],
            popup=folium.Popup(popup_text, max_width=450, sticky=True),
            icon=folium.features.DivIcon(
                # icon_size=(150, 36),
                icon_anchor=(-5, -5),
                html='<div style="'
                + "font-size: 20pt;"
                + "color: white;"
                + "text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000;"
                + f'">{abbreviations[point[1]]}</div>',
            ),
        )
        text.add_to(m)

    # Add layer control (needs to be added after all elements are added)
    folium.LayerControl().add_to(m)

    # Save the map
    m.save("compass.html")


if __name__ == "__main__":
    plot_compass()
