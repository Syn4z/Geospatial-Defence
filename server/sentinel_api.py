# Utilities
import matplotlib.pyplot as plt
import pandas as pd
import getpass

from sentinelhub import (
    SHConfig,
    DataCollection,
    SentinelHubCatalog,
    SentinelHubRequest,
    SentinelHubStatistical,
    BBox,
    bbox_to_dimensions,
    CRS,
    MimeType,
    Geometry,
)

def set_up_sentinelhub_config(client_id, client_secret):
    """
    Set up the Sentinel Hub configuration with the provided client ID and client secret.

    This function initializes and configures the Sentinel Hub settings, including the client ID,
    client secret, token URL, and base URL. The configuration is then saved with the name "cdse".

    Args:
        client_id (str): The client ID for accessing Sentinel Hub services.
        client_secret (str): The client secret for accessing Sentinel Hub services.

    Returns:
        SHConfig: The configured Sentinel Hub configuration object.
    """
    # Set up Sentinel Hub configuration
    config = SHConfig()
    config.sh_client_id = client_id
    config.sh_client_secret = client_secret
    config.sh_token_url = "https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token"
    config.sh_base_url = "https://sh.dataspace.copernicus.eu"
    config.save("cdse")
    return config

def get_sentinelhub_image(config, coords, time_interval, resolution=10, distance=1):
    """
    Fetches a true color image from Sentinel Hub for a given area of interest (AOI) and time interval.

    Args:
        config (SentinelHubConfig): Configuration object for Sentinel Hub.
        coords (tuple): A tuple of (longitude, latitude) representing the center of the AOI.
        time_interval (tuple): A tuple of (start_date, end_date) in the format 'YYYY-MM-DD'.
        resolution (int, optional): Spatial resolution of the requested image in meters. Default is 10.
        distance (int, optional): Distance in degrees to define the size of the AOI around the center coordinates. Default is 1.

    Returns:
        numpy.ndarray: A true color image as a NumPy array.
    """
    
    km_long = 1 / 111.32 * distance
    km_lat = 1 / 110.574 * distance
    aoi_coords_wgs84 = [
        coords[0] - km_long,
        coords[1] - km_lat,
        coords[0] + km_long,
        coords[1] + km_lat,
    ]

    aoi_bbox = BBox(bbox=aoi_coords_wgs84, crs=CRS.WGS84)
    aoi_size = bbox_to_dimensions(aoi_bbox, resolution=resolution)

    # Get Sentinel Hub catalog
    catalog = SentinelHubCatalog(config=config)
    aoi_bbox = BBox(bbox=aoi_coords_wgs84, crs=CRS.WGS84)
    time_interval = (time_interval[0], time_interval[1])

    search_iterator = catalog.search(
        DataCollection.SENTINEL2_L2A,
        bbox=aoi_bbox,
        time=time_interval,
        fields={"include": ["id", "properties.datetime"], "exclude": []},
    )

    results = list(search_iterator)

    evalscript_true_color = """
        //VERSION=3

        function setup() {
            return {
                input: [{
                    bands: ["B02", "B03", "B04"]
                }],
                output: {
                    bands: 3
                }
            };
        }

        function evaluatePixel(sample) {
            return [sample.B04, sample.B03, sample.B02];
        }
    """

    request_true_color = SentinelHubRequest(
        evalscript=evalscript_true_color,
        input_data=[
            SentinelHubRequest.input_data(
                data_collection=DataCollection.SENTINEL2_L2A.define_from(
                    name="s2l2a", service_url="https://sh.dataspace.copernicus.eu"
                ),
                time_interval = (time_interval[0], time_interval[1]),
                other_args={"dataFilter": {"mosaickingOrder": "leastCC", "maxCloudCoverage": 50}},
            )
        ],
        responses=[SentinelHubRequest.output_response("default", MimeType.PNG)],
        bbox=aoi_bbox,
        size=aoi_size,
        config=config,
    )

    img = request_true_color.get_data()[0]

    return img

def get_sentinelhub_colored_img(config, coords, time_interval, resolution=10, distance=1):
    """
    Fetches a Sentinel-2 image with NDMI (Normalized Difference Moisture Index) coloring.
    Args:
        config (SentinelHubConfig): Configuration object for Sentinel Hub.
        coords (tuple): A tuple of (longitude, latitude) representing the center coordinates.
        time_interval (tuple): A tuple of (start_date, end_date) in 'YYYY-MM-DD' format.
        resolution (int, optional): Spatial resolution of the image in meters. Defaults to 10.
        distance (int, optional): Distance in kilometers from the center coordinates to define the area of interest. Defaults to 1.
    Returns:
        numpy.ndarray: A 4-band image array with NDMI coloring and data mask.
    """

    evalscript_ndmi = """
    //VERSION=3
    function setup() {
    return {
        input: [{
        bands: [
            "B08",
            "B11",
            "dataMask"
        ]
        }],
        output: {
        bands: 4
        }
    }
    }

    function evaluatePixel(sample) {
        let ndmi = (sample.B08 - sample.B11) / (sample.B08 + sample.B11);
        let imgVals = null;
        
        if (ndmi < -1.0) imgVals = [1, 0, 0]; // Red
        else if (ndmi < -0.5) imgVals = [1, 0.1, 0]; // Red fading to orange
        else if (ndmi < 0.0) imgVals = [1, 0.5, 0]; // Orange to yellow
        else if (ndmi < 0.25) imgVals = [0.75, 0.5, 0.3]; // Yellow to light green
        else if (ndmi < 0.5) imgVals = [0, 0.7, 0.3]; // Light green to green
        else if (ndmi < 0.75) imgVals = [0, 0.5, 1]; // Green to blue
        else imgVals = [0, 0, 1]; // Full blue

        
        imgVals.push(sample.dataMask);
        
        return imgVals;
    }
    """

    km_long = 1 / 111.32 * distance
    km_lat = 1 / 110.574 * distance
    aoi_coords_wgs84 = [
        coords[0] - km_long,
        coords[1] - km_lat,
        coords[0] + km_long,
        coords[1] + km_lat,
    ]

    aoi_bbox = BBox(bbox=aoi_coords_wgs84, crs=CRS.WGS84)
    aoi_size = bbox_to_dimensions(aoi_bbox, resolution=resolution)

    request_ndmi_img = SentinelHubRequest(
        evalscript=evalscript_ndmi,
        input_data=[
            SentinelHubRequest.input_data(
                data_collection=DataCollection.SENTINEL2_L2A.define_from(
                    name="s2l2a", service_url="https://sh.dataspace.copernicus.eu"
                ),
                time_interval=(time_interval[0], time_interval[1]),
                other_args={"dataFilter": {"mosaickingOrder": "leastCC"}},
            )
        ],
        responses=[SentinelHubRequest.output_response("default", MimeType.PNG)],
        bbox=aoi_bbox,
        size=aoi_size,
        config=config,
    )

    img = request_ndmi_img.get_data()[0]

    return img




