#whatever version that suits you
FROM rasa/rasa:2.7.2 

#define the working directory of Docker container
WORKDIR /app 

#copy everything in ./actions directory (your custom actions code) to /app/actions in container
COPY ./ ./

EXPOSE 5005

USER root
RUN chmod +x ./entrypoint.sh
USER 1001

#CMD $(echo "rasa run -p $PORT")
# Run the generated shell script.
ENTRYPOINT ["./entrypoint.sh"]
#CMD ['run', 'rasa', '-p', '5005', '--cors', '*', '--enable-api'] 