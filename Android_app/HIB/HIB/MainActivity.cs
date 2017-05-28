using Android.App;
using Android.Widget;
using Android.OS;
using System.Json;
using System.Threading.Tasks;
using System.Net;
using System.IO;
using System;
using Android.Graphics;
using Android.Content;

namespace HIB
{
    [Activity(Label = "HIB Application", MainLauncher = true, Icon = "@drawable/icon")]

    public class MainActivity : Activity
    {
        protected override void OnCreate(Bundle bundle)
        {
            base.OnCreate(bundle);

            // Set our view from the "main" layout resource
            SetContentView(Resource.Layout.Main);


            Button b = FindViewById<Button>(Resource.Id.button1);
            Button routeHistoryButton = FindViewById<Button>(Resource.Id.routeHistoryButton);
            b.Click += async (sender, e) =>
            {
                // thingspeak cloud service unique url 
                // todo for current id
                string url = "https://api.thingspeak.com/channels/278656/feeds.json?api_key=9D1RVB2L4LN7U5N2";

                // Fetch the weather information asynchronously, 
                // parse the results, then update the screen:
                JsonValue json = await FetchData(url);
                ParseAndDisplay(json);
            };

            routeHistoryButton.Click += (sender, e) =>
            {
                var intent = new Intent(this, typeof(Activity1));
                //intent.PutStringArrayListExtra("phone_numbers", phoneNumbers);
                StartActivity(intent);
            };
        }


        private async Task<JsonValue> FetchData(string url)
        {
            HttpWebRequest request = (HttpWebRequest)HttpWebRequest.Create(new Uri(url));
            request.ContentType = "application/json";
            request.Method = "GET";

            using (WebResponse response = await request.GetResponseAsync())
            {
                using (Stream stream = response.GetResponseStream())
                {
                    // Use this stream to build a JSON document object:
                    JsonValue jsonDoc = await Task.Run(() => JsonObject.Load(stream));
                    Console.Out.WriteLine("Response: {0}", jsonDoc.ToString());

                    return jsonDoc;
                }
            }

          
        }



        private void ParseAndDisplay(JsonValue json)
        {
            TextView t1 = FindViewById<TextView>(Resource.Id.textView1);
            TextView t2 = FindViewById<TextView>(Resource.Id.textView2);
            TextView t3 = FindViewById<TextView>(Resource.Id.textView3);
            TextView t4 = FindViewById<TextView>(Resource.Id.textView4);

            // feeds is what we want
            JsonValue feeds = json["feeds"];

            int? field1 = null;
            foreach (JsonValue feed in feeds)
            {
                field1 = ConvertToNumber(feed["field1"]);
                if (field1 != null)
                {
                    Console.WriteLine(field1);
                    if (field1 < 40)
                    {
                        t1.Text = feed["field1"];
                    }
                    else if (field1 < 60)
                    {
                        t3.Text = feed["field1"];
                        t3.SetTextColor(Color.White);
                    }
                    else if (field1 < 90)
                    {
                        t4.Text = feed["field1"];
                        t4.SetTextColor(Color.Yellow);
                    }

                }
            }

        }


        public int? ConvertToNumber(JsonValue jv)
        {
            int outValue;
            return int.TryParse((string)jv, out outValue) ? (int?)outValue : null;
        }
    }
}

